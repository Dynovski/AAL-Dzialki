# |---------------------|  x - punkt przecięcia
# |          |          |  A, B, C, D - pod-obszary po przecięciu
# |    A     |     B    |
# |          |          |
# |----------x----------|
# |          |          |
# |    D     |     C    |
# |          |          |
# |---------------------|
from utilities.field_calculator import calculate_max_num_of_fields


class PointOfIntersection:
    def __init__(self, coordinates, all_points):
        self.coordinates = coordinates
        self.points_a = []
        self.points_b = []
        self.points_c = []
        self.points_d = []

        for point in all_points:
            if point[0] < coordinates[0] and point[1] > coordinates[1]:
                self.points_a.append(point)
            elif point[0] > coordinates[0] and point[1] > coordinates[1]:
                self.points_b.append(point)
            elif point[0] < coordinates[0] and point[1] < coordinates[1]:
                self.points_d.append(point)
            elif point[0] > coordinates[0] and point[1] < coordinates[1]:
                self.points_c.append(point)

        # Obliczanie największej liczby możliwych działek
        self.max_num_of_fields = calculate_max_num_of_fields(len(self.points_a)) + \
            calculate_max_num_of_fields(len(self.points_b)) + \
            calculate_max_num_of_fields(len(self.points_c)) + \
            calculate_max_num_of_fields(len(self.points_d))

    def __lt__(self, other):
        return self.max_num_of_fields < other.max_num_of_fields
