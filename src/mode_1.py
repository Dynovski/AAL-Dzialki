from zone import Zone


def parse(string):
    x, y = string.split(sep=",")
    return int(x), int(y)


def read_data(filename):
    # Automatycznie zamyka plik nawet jeśli podniesiony będzie wyjątek
    with open(filename, 'r') as file:
        width, height = parse(file.readline())

        points = []
        for line in file:
            x, y = parse(line)
            if not (0 < x < width and 0 < y < height):
                raise ValueError(f"Point is not within range of zone: ({x}, {y})")
            points.append((x, y))

        if len(points) >= min(width, height):
            raise ValueError("Too many points for a given zone size")

        return Zone(0, width, height, 0, points)


def store_answer(filename, answer):
    with open(filename, 'w') as file:
        file.write(f"Maximum number of fields: {answer[0]}\nIntersection points in sequence: {answer[1]}")
