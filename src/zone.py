# |---------------------|  x - punkt przecięcia
# |          |          |  A, B, C, D - podobszary po przecięciu
# |    A     |     B    |
# |          |          |
# |----------x----------|
# |          |          |
# |    D     |     C    |
# |          |          |
# |---------------------|
from considered_point_of_intersection import ConsideredPointOfIntersection
import heapq


class Zone:
    def __init__(self, x_left, x_right, y_top, y_bottom, points):
        self.x_left = x_left
        self.x_right = x_right
        self.y_top = y_top
        self.y_bottom = y_bottom
        self.points = sorted(points, key=lambda point: point[1])
        self.priority_queue = []

    def solve(self, x=0):
        print("    " * x + f"Entered solve() level {x}")
        print("    " * x + "All points:", self.points)
        if len(self.points) == 0:
            print("    " * x + "Result +0")
            return 0, []
        elif len(self.points) == 1:
            print("    " * x + "Result +1")
            return 1, []
        elif len(self.points) == 2:
            print("    " * x + "Result +1")
            # Dobolny punkt, nie ma znaczenie w tym wypadku
            return 1, [self.points[0]]
        elif len(self.points) == 3:
            print("    " * x + "Result +2")
            # Punkty są posortowane, zwracamy środkowy
            return 2, [self.points[1]]

        best_intersection_point = []
        best_trace = []
        best_result = 0

        for point in self.points:
            p = ConsideredPointOfIntersection(point, self.points)
            priority = -p.max_num_of_fields
            heapq.heappush(self.priority_queue, (priority, p))

        while True:
            cp = heapq.heappop(self.priority_queue)[1]
            print("    " * x + f"Max number od fields for {cp.intersection_point}: {cp.max_num_of_fields}")
            # 0 --> Obszar A, 1 --> Obszar B, 2 --> Obszar C, 3 --> Obszar D
            zones = (Zone(self.x_left, cp.intersection_point[0], self.y_top, cp.intersection_point[1], cp.points_a),
                     Zone(cp.intersection_point[0], self.x_right, self.y_top, cp.intersection_point[1], cp.points_b),
                     Zone(self.x_left, cp.intersection_point[0], cp.intersection_point[1], self.y_bottom, cp.points_c),
                     Zone(cp.intersection_point[0], self.x_right, cp.intersection_point[1], self.y_bottom, cp.points_d))
            # Dane lokalne dla danego rozpatrywanego punktu przecięcia, usuwane jeśli nie jest on optymalny
            result = 0
            trace = []
            for zone in zones:
                new_result, existing_trace = zone.solve(x + 1)
                result += new_result
                trace += existing_trace
                print("    " * x + "Current result:", result)

            if result > best_result:
                best_intersection_point = [cp.intersection_point]
                best_trace = trace
            best_result = max(best_result, result)
            print("    " * x + f"Best result for point {cp.intersection_point}: {best_result}")
            try:
                # Jeśli obecny wynik nie może być poprawiony w optymistycznym przypadku
                if best_result >= -self.priority_queue[0][0]:
                    return best_result, best_intersection_point + best_trace
            # Gdy jesteśmy w ostatnim punkcie
            except IndexError:
                return best_result, best_intersection_point + best_trace

    def __str__(self):
        return f"""Left border: {self.x_left}
Right border: {self.x_right}
Top border: {self.y_top}
Bottom border: {self.y_bottom}
Points: {self.points}"""
