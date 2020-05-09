from zone import Zone


def parse_zone(string):
    width, height = string.split(sep=",")
    return int(width), int(height)


def parse_point(string):
    x, y = string.split(sep=",")
    return int(x), int(y)


def read_data(filename):
    # Automatycznie zamyka plik nawet jeśli podniesiony będzie wyjątek
    with open(filename, 'r') as file:
        width, height = parse_zone(file.readline())

        points = []
        for line in file:
            points.append(parse_point(line))

        if len(points) >= min(width, height):
            raise ValueError("Too many specified points to create in a given zone size")

        return Zone(0, width, height, 0, points)
