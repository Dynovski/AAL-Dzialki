import matplotlib.pyplot as plt
from zone import Zone
from point_of_intersection import PointOfIntersection


def draw_initial_state(points, width, height):
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
    plt.plot((point[0], restrictions[1]), (point[1], point[1]), color="red")
    plt.plot((point[0], restrictions[0]), (point[1], point[1]), color="red")
    plt.plot((point[0], point[0]), (point[1], restrictions[2]), color="red")
    plt.plot((point[0], point[0]), (point[1], restrictions[3]), color="red")


def append_sub_zones(zones, from_zone, intersection_point):
    zones.append(Zone(from_zone.x_left, intersection_point.coordinates[0], from_zone.y_top,
                      intersection_point.coordinates[1], intersection_point.points_a))
    zones.append(Zone(intersection_point.coordinates[0], from_zone.x_right, from_zone.y_top,
                      intersection_point.coordinates[1], intersection_point.points_b))
    zones.append(Zone(from_zone.x_left, intersection_point.coordinates[0], intersection_point.coordinates[1],
                      from_zone.y_bottom, intersection_point.points_c))
    zones.append(Zone(intersection_point.coordinates[0], from_zone.x_right, intersection_point.coordinates[1],
                      from_zone.y_bottom, intersection_point.points_d))


def draw_problem(start_zone, answer):
    draw_initial_state(start_zone.points, start_zone.x_right, start_zone.y_top)

    zones = [start_zone]

    while answer:
        intersection_coordinates = answer.pop(0)

        # Przeglądamy obszary od największych i jeśli punkt jest w tym obszarze to tniemy i usuwamy obszar z listy
        for i in range(len(zones)):
            if zones[i].contains(intersection_coordinates):
                intersection_point = PointOfIntersection(intersection_coordinates, zones[i].points)
                intersect_in_point(intersection_coordinates, (zones[i].x_left, zones[i].x_right,
                                                              zones[i].y_top, zones[i].y_bottom))
                append_sub_zones(zones, zones[i], intersection_point)
                zones.pop(i)
                break
    plt.show()
