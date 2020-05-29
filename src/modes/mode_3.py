import time
import math
import sys
from modes.mode_2 import generate_instance
from prettytable import PrettyTable


def measure_mean_execution_time(function, repetitions):
    start_time = time.process_time()
    for _ in range(repetitions):
        function({})
    return (time.process_time() - start_time) / repetitions


def benchmark(width, height, start_number, step, iterations, repetitions):
    """Generuje coraz trudniejsze instancje problemu oraz oblicza średni czas potrzebny do ich rozwiązania, rezultat zapisywany jest do pliku test_results.txt"""
    with open("test_results.txt", 'w') as file:
        file.write(f"Benchmarking for {iterations} iterations\n"
                   f"Initial parameters:\n"
                   f"width - {width}\n"
                   f"height - {height}\n"
                   f"number of points - {start_number}\n"
                   f"step - {step}\n"
                   f"iterations - {iterations}\n"
                   f"repetitions - {repetitions}\n\n")

    mean_times = []

    for i in range(iterations):
        num_of_points = start_number + i * step
        zone_width = width + i * step
        zone_height = height + i * step

        problem = generate_instance(zone_width, zone_height, num_of_points)

        mean_times.append(measure_mean_execution_time(problem.solve, repetitions))

    time_median = mean_times[iterations // 2]
    n_median = start_number + (iterations // 2) * step

    optimistic_coefficient = time_median / (n_median * math.log(n_median, 4))
    square_coefficient = time_median / (n_median ** 2)
    cube_coefficient = time_median / (n_median ** 3)
    quarto_coefficient = time_median / (n_median ** 4)
    n_to_fifth_coefficient = time_median / (n_median ** 5)
    two_to_n_coefficient = time_median
    pessimistic_coefficient = time_median
    # Zabezpieczenie przed zbyt dużymi wartościami
    try:
        two_to_n_coefficient /= (2 ** n_median)
        pessimistic_coefficient /= (n_median ** n_median)
    except OverflowError:
        two_to_n_coefficient /= sys.float_info.max
        pessimistic_coefficient /= sys.float_info.max

    table = PrettyTable(['n', 't(n) [s]', 'O(nlogn) q(n)', 'O(n^2) q(n)', 'O(n^3) q(n)',
                         'O(n^4) q(n)', 'O(n^5) q(n)', 'O(2^n) q(n)', 'O(n^n) q(n)'])

    print(mean_times)

    for i in range(iterations):
        current_n = start_number + i * step
        # Zabezpieczenie gdy current_n ** current_n jest za duże żeby przekonwertować na float
        try:
            table.add_row([f"{current_n}", f"{mean_times[i]:.8f}",
                           f"{mean_times[i] / (optimistic_coefficient * current_n * math.log(current_n, 4)):.5}",
                           f"{mean_times[i] / (square_coefficient * current_n ** 2):.5}",
                           f"{mean_times[i] / (cube_coefficient * current_n ** 3):.5}",
                           f"{mean_times[i] / (quarto_coefficient * current_n ** 4):.5}",
                           f"{mean_times[i] / (n_to_fifth_coefficient * current_n ** 5):.5}",
                           f"{mean_times[i] / (two_to_n_coefficient * 2 ** current_n):.5}",
                           f"{mean_times[i] / (pessimistic_coefficient * current_n ** current_n):.5}"])
        except OverflowError:
            # Zabezpieczenie gdy 2 ** current_n jest za duże żeby przekonwertować na float
            try:
                table.add_row([f"{current_n}", f"{mean_times[i]:.8f}",
                               f"{mean_times[i] / (optimistic_coefficient * current_n * math.log(current_n, 4)):.5}",
                               f"{mean_times[i] / (square_coefficient * current_n ** 2):.5}",
                               f"{mean_times[i] / (cube_coefficient * current_n ** 3):.5}",
                               f"{mean_times[i] / (quarto_coefficient * current_n ** 4):.5}",
                               f"{mean_times[i] / (n_to_fifth_coefficient * current_n ** 5):.5}",
                               f"{mean_times[i] / (two_to_n_coefficient * 2 ** current_n):.5}",
                               "0.0"])
            except OverflowError:
                table.add_row([f"{current_n}", f"{mean_times[i]:.8f}",
                               f"{mean_times[i] / (optimistic_coefficient * current_n * math.log(current_n, 4)):.5}",
                               f"{mean_times[i] / (square_coefficient * current_n ** 2):.5}",
                               f"{mean_times[i] / (cube_coefficient * current_n ** 3):.5}",
                               f"{mean_times[i] / (quarto_coefficient * current_n ** 4):.5}",
                               f"{mean_times[i] / (n_to_fifth_coefficient * current_n ** 5):.5}",
                               "0.0",
                               "0.0"])

    with open("test_results.txt", 'a') as file:
        file.write(f"{table}\n")


