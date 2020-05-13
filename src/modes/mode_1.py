from classes.zone import Zone


def parse(string):
    x, y = string.split(sep=",")
    return int(x), int(y)


def read_data(filename):
    """Wczytuje dane z pliku i na ich podstawie tworzy instancję obszaru początkowego"""
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

        validate_coordinates(points)

        return Zone(0, width, height, 0, points)


def store_answer(filename, answer):
    with open(filename, 'w') as file:
        file.write(f"Maximum number of fields: {answer[0]}\nIntersection points in sequence: {answer[1]}")


def validate_coordinates(points):
    """Sprawdza, czy żadne dwa punkty nie mają takiej samej współrzędnej"""
    x_list, y_list = zip(*points)
    for i in x_list:
        if x_list.count(i) > 1:
            raise ValueError("There are points with the same x coordinate")

    for j in y_list:
        if y_list.count(j) > 1:
            raise ValueError("There are points with the same y coordinate")

