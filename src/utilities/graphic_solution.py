import matplotlib.pyplot as plt
from classes.zone import Zone
from classes.point_of_intersection import PointOfIntersection


def prepare_plot(points, width, height):
    """Oznacza osi współrzędnych oraz rysuje punkty"""
    x, y = zip(*points)
    plt.scatter(x, y)
    plt.xlim(0, width)
    plt.ylim(0, height)
    plt.xticks(range(0, width + 1))
    plt.yticks(range(0, height + 1))
    plt.grid(True)
    plt.xlabel("Width")
    plt.ylabel("Height")


# restrictions[0] - lewo, restrictions[1] - prawo, restrictions[2] - góra, restrictions[3] - dół
def intersect_in_point(point, restrictions):
    """Prowadzi proste od punktów do końca najbliższego obszaru w lewo, prawo, górę i dół"""
    plt.plot((point[0], restrictions[1]), (point[1], point[1]), color="red")
    plt.plot((point[0], restrictions[0]), (point[1], point[1]), color="red")
    plt.plot((point[0], point[0]), (point[1], restrictions[2]), color="red")
    plt.plot((point[0], point[0]), (point[1], restrictions[3]), color="red")


def append_subzones(zones_list, of_zone, intersection_point):
    """Dodaje nowe obszary do listy po przecięciu w danym punkcie"""
    zones_list.append(Zone(of_zone.x_left, intersection_point.coordinates[0], of_zone.y_top,
                           intersection_point.coordinates[1], intersection_point.points_a))
    zones_list.append(Zone(intersection_point.coordinates[0], of_zone.x_right, of_zone.y_top,
                           intersection_point.coordinates[1], intersection_point.points_b))
    zones_list.append(Zone(of_zone.x_left, intersection_point.coordinates[0], intersection_point.coordinates[1],
                           of_zone.y_bottom, intersection_point.points_c))
    zones_list.append(Zone(intersection_point.coordinates[0], of_zone.x_right, intersection_point.coordinates[1],
                           of_zone.y_bottom, intersection_point.points_d))


def draw(start_zone, list_of_intersection_point):
    """Rysuje cięcia obszarów i powstały w ten sposób stan końcowy obszaru początkowego"""
    prepare_plot(start_zone.points, start_zone.x_right, start_zone.y_top)
    zones = [start_zone]

    while list_of_intersection_point:
        intersection_coordinates = list_of_intersection_point.pop(0)

        # Przeglądamy obszary od największych i jeśli punkt jest w tym obszarze to tniemy i usuwamy obszar z listy
        for i in range(len(zones)):
            if zones[i].contains(intersection_coordinates):
                intersection_point = PointOfIntersection(intersection_coordinates, zones[i].points)
                intersect_in_point(intersection_coordinates, (zones[i].x_left, zones[i].x_right,
                                                              zones[i].y_top, zones[i].y_bottom))
                append_subzones(zones, zones[i], intersection_point)
                zones.pop(i)
                break
    plt.show()
