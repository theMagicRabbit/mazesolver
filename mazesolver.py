from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, line_color: str):
        canvas.create_line((self.p1.x, self.p1.y), (self.p2.x, self.p2.y), fill=line_color, width=16)

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

class Cell():
    def __init__(self, x1, y1, x2, y2, window, top_side=True, right_side=True, bottom_side=True, left_side=True):
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

    def __repr__(self):
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2}, {self.has_top}, {self.has_right}, {self.has_bottom}, {self.has_left})"

class Window():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.root_widget = Tk()
        self.root_widget.title("mazesolver")
        self.canvas = Canvas(width=self.width, height=self.height)
        self.canvas.pack()
        self.is_running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line: Line, fill_color: str):
        print(line)
        line.draw(self.canvas, fill_color)
    def __repr__(self):
        return f"Window({self.width}, {self.height})"

def main():
    win = Window(800, 600)
    cells = [
        Cell(110, 110, 111, 111, win, True, True, True, True),
        Cell(700, 500, 701, 501, win, True, True, True, False),
        Cell(100, 101, 101, 102, win, True, True, False, True),
        Cell(200, 200, 201, 201, win, True, False, True, True),
        Cell(300, 300, 301, 301, win, False, True, True, True),
        Cell(400, 400, 401, 401, win, True, True, False, False),
        Cell(500, 500, 501, 501, win, True, False, False, False),
        Cell(600, 510, 601, 511, win, True, False, True, False),
        Cell(650, 510, 651, 511, win, False, False, False, False),
    ]
    for c in cells:
        c.draw()
    win.wait_for_close()

if __name__ == '__main__':
    main()

