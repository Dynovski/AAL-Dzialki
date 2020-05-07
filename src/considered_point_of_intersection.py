# |---------------------|  x - punkt przecięcia
# |          |          |  A, B, C, D - podobszary po przecięciu
# |    A     |     B    |
# |          |          |
# |----------x----------|
# |          |          |
# |    D     |     C    |
# |          |          |
# |---------------------|


class ConsideredPointOfIntersection:
    def __init__(self, intersection_point, all_points):
        self.intersection_point = intersection_point
        self.points_a = []
        self.points_b = []
        self.points_c = []
        self.points_d = []
        self._correction = (3, 1, 1, 2)

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
        self.max_num_of_fields = len(self.points_a) // 4 * 3 + self._correction[len(self.points_a) % 4] + \
            len(self.points_b) // 4 * 3 + self._correction[len(self.points_b) % 4] + \
            len(self.points_c) // 4 * 3 + self._correction[len(self.points_c) % 4] + \
            len(self.points_d) // 4 * 3 + self._correction[len(self.points_d) % 4]
