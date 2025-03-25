from lines import Point, Line


class Cell:
    def __init__(self, x1, y1, x2, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def draw(self):
        if self.has_left_wall:
            left_line = Line(Point(self._x1, self._y1),
                             Point(self._x1, self._y2))
            self._win.draw_line(left_line, "blue")
            print("left line")
        if self.has_right_wall:
            right_line = Line(Point(self._x2, self._y1),
                              Point(self._x2, self._y2))
            self._win.draw_line(right_line, "red")
            print("right line")
        if self.has_top_wall:
            top_line = Line(Point(self._x1, self._y1),
                            Point(self._x2, self._y1))
            self._win.draw_line(top_line, "black")
            print("top line")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self._x1, self._y2),
                               Point(self._x2, self._y2))
            self._win.draw_line(bottom_line, "green")
            print("bottom line")
