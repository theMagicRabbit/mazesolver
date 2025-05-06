from mazesolver import Point, Line

class Cell():
    def __init__(self, x1, y1, x2, y2, window=None, top_side=True, right_side=True, bottom_side=True, left_side=True):
        self.has_top = top_side
        self.has_right = right_side
        self.has_bottom = bottom_side
        self.has_left = left_side
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self.top_left = Point(x1, y1)
        self.top_right = Point(x2, y1)
        self.bottom_left = Point(x1, y2)
        self.bottom_right = Point(x2, y2)
        self._window = window

    def draw(self):
        sides = []
        if self.has_top:
            sides.append(Line(self.top_left, self.top_right))
        if self.has_left:
            sides.append(Line(self.top_left, self.bottom_left))
        if self.has_right:
            sides.append(Line(self.top_right, self.bottom_right))
        if self.has_bottom:
            sides.append(Line(self.bottom_left, self.bottom_right))
        for s in sides:
            self._window.draw_line(s, "green")

    def draw_move(self, to_cell, undo=False):
        dx = (x2 - x1) / 2
        dy = (y2 - y1) / 2
        start = Point(self._x1 + abs(dx), self._y1 + abs(dy))
        end = Point(to_cell._x1 + abs(dx), to_cell._y1 + abs(dy))
        line = Line(start, end)
        if undo:
            color = "gray"
        else:
            color = "red"
        self._window.draw_line(line, color)

    def __repr__(self):
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2}, {self.has_top}, {self.has_right}, {self.has_bottom}, {self.has_left})"

