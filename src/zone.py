class Zone:
    def __init__(self, x_left, x_right, y_top, y_bottom, points):
        self.x_left = x_left
        self.x_right = x_right
        self.y_top = y_top
        self.y_bottom = y_bottom
        self.points = sorted(points, key=lambda point: point[1])

    def contains(self, point):
        return self.x_left < point[0] < self.x_right and self.y_bottom < point[1] < self.y_top

