import time
from modes.mode_2 import generate_instance
import matplotlib.pyplot as plt


def measure_mean_execution_time(function, repetitions, solved):
    start_time = time.process_time()
    for _ in range(repetitions):
        function(solved)
    return (time.process_time() - start_time) / repetitions


def benchmark(width, height, start_number, step, iterations, repetitions, solved):
    """Generuje coraz trudniejsze instancje problemu oraz oblicza średni czas potrzebny do ich rozwiązania, rezultat zapisywany jest do pliku test_results.txt"""
    open("test_results.txt", 'w').close()

    for i in range(iterations):
        num_of_points = start_number + i * step
        zone_width = width + i * step
        zone_height = height + i * step

        problem = generate_instance(zone_width, zone_height, num_of_points)

        mean_time = measure_mean_execution_time(problem.solve, repetitions, solved)

        with open("test_results.txt", 'a') as file:
            file.write(f"Iteration: {i + 1}, problem size: {num_of_points}\n"
                       f"Generated problem:\n{problem}\n"
                       f"Mean time of execution: {mean_time}\n\n")

