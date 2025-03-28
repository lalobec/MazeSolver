from lines import Point, Line


class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        if not self._win:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line, "black")
        else:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line, "#d9d9d9")
        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line, "black")
        else:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line, "#d9d9d9")
        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line, "black")
        else:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line, "#d9d9d9")
        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line, "black")
        else:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        cellcenterA_x = (self._x1 + self._x2) / 2
        cellcenterA_y = (self._y1 + self._y2) / 2
        centerA = Point(cellcenterA_x, cellcenterA_y)
        cellcenterB_x = (to_cell._x1 + to_cell._x2) / 2
        cellcenterB_y = (to_cell._y1 + to_cell._y2) / 2
        centerB = Point(cellcenterB_x, cellcenterB_y)
        lineAB = Line(centerA, centerB)

        fill_color = "red"
        if undo:
            fill_color = "gray"

        self._win.draw_line(lineAB, fill_color)
