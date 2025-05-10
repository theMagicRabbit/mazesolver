from mazesolver import Point, Line

class Cell():
    def __init__(self, win=None):
        self.has_top = True
        self.has_right = True 
        self.has_bottom = True 
        self.has_left = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.visited = False
        self._win = win

    def draw(self, x1, y1, x2, y2):
        sides = []
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        sides.append((self.has_top, Line(Point(x1, y1), Point(x2, y1))))
        sides.append((self.has_left, Line(Point(x1, y1), Point(x1, y2))))
        sides.append((self.has_right, Line(Point(x2, y1), Point(x2, y2))))
        sides.append((self.has_bottom, Line(Point(x1, y2), Point(x2, y2))))
        for is_vis, side in sides:
            if is_vis:
                if self._win:
                    self._win.draw_line(side, "black")
            else:
                if self._win:
                    self._win.draw_line(side, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return
        if not self._x1 or not self._x2 or not self._y1 or not self._y2:
            raise Exception("Cell not defined")
        dx = (self._x2 - self._x1) / 2
        dy = (self._y2 - self._y1) / 2
        start = Point(self._x1 + abs(dx), self._y1 + abs(dy))
        end = Point(to_cell._x1 + abs(dx), to_cell._y1 + abs(dy))
        line = Line(start, end)
        if undo:
            color = "gray"
        else:
            color = "red"
        self._win.draw_line(line, color)

    def __repr__(self):
        return f"Cell({self._win})"

    def __str__(self):
        return (f"Cell({self.has_top}, {self.has_right}, {self.has_bottom}, {self.has_left}, "
                f"{self._x1}, {self._x2}, {self._y1}, {self._y2}, {self.visited})")

