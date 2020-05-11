from random import shuffle
from zone import Zone


def generate_instance(width, height, num_of_points):
    if num_of_points >= min(width, height):
        raise ValueError("Too many points for a given zone size")
    point_x = [*range(1, width)]
    point_y = [*range(1, height)]

    shuffle(point_x)
    shuffle(point_y)

    points = []

    for _ in range(num_of_points):
        new_point = (point_x.pop(), point_y.pop())
        points.append(new_point)

    return Zone(0, width, height, 0, points)


def store_answer(start_zone, answer, filename="output.txt"):
    with open(filename, 'w') as file:
        file.write(f"Generated problem:\n{start_zone}\n\n"
                   f"Maximum number of fields: {answer[0]}\nIntersection points in sequence: {answer[1]}")
