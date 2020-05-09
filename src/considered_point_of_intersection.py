# |---------------------|  x - punkt przecięcia
# |          |          |  A, B, C, D - podobszary po przecięciu
# |    A     |     B    |
# |          |          |
# |----------x----------|
# |          |          |
# |    D     |     C    |
# |          |          |
# |---------------------|
from optimistic_field_calculator import calculate_max_num_of_fields


class ConsideredPointOfIntersection:
    def __init__(self, intersection_point, all_points):
        self.intersection_point = intersection_point
        self.points_a = []
        self.points_b = []
        self.points_c = []
        self.points_d = []

        for point in all_points:
            if point[0] < intersection_point[0] and point[1] > intersection_point[1]:
                self.points_a.append(point)
            elif point[0] > intersection_point[0] and point[1] > intersection_point[1]:
                self.points_b.append(point)
            elif point[0] < intersection_point[0] and point[1] < intersection_point[1]:
                self.points_d.append(point)
            elif point[0] > intersection_point[0] and point[1] < intersection_point[1]:
                self.points_c.append(point)

        # Obliczanie największej liczby możliwych działek
        self.max_num_of_fields = calculate_max_num_of_fields(len(self.points_a)) + \
            calculate_max_num_of_fields(len(self.points_b)) + \
            calculate_max_num_of_fields(len(self.points_c)) + \
            calculate_max_num_of_fields(len(self.points_d))

    def __lt__(self, other):
        return self.max_num_of_fields < other.max_num_of_fields
