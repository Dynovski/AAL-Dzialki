import time
from mode_2 import generate_instance


def measure_mean_execution_time(function, repetitions):
    start_time = time.process_time()
    for _ in range(repetitions):
        function()
    return (time.process_time() - start_time) / repetitions


def start_testing(width, height, start_number, step, iterations, repetitions):
    open("test_results.txt", 'w').close()
    for i in range(iterations):
        num_of_points = start_number + i * step
        zone_width = width + i * step
        zone_height = height + i * step

        problem = generate_instance(zone_width, zone_height, num_of_points)

        mean_time = measure_mean_execution_time(problem.solve, repetitions)

        with open("test_results.txt", 'a') as file:
            file.write(f"Iteration: {i + 1}, problem size: {num_of_points}\n"
                       f"Generated problem:\n{problem}\n"
                       f"Mean time of execution: {mean_time}\n\n")

