from tkinter import Tk, BOTH, Canvas
from time import sleep

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
        start = Point(self._x1 + 0.5, self._y1 + 0.5)
        end = Point(to_cell._x1 + 0.5, to_cell._y1 + 0.5)
        line = Line(start, end)
        if undo:
            color = "gray"
        else:
            color = "red"
        self._window.draw_line(line, color)

    def __repr__(self):
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2}, {self.has_top}, {self.has_right}, {self.has_bottom}, {self.has_left})"

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for x in range(self._num_rows):
            row = []
            for y in range(self._num_cols):
                row.append(Cell(x, y, x + self._cell_size_x, y + self._cell_size_y, self._win))
            self._cells.append(row)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    def _animate(self):
        self._win.redraw()

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
    maze = Maze(0, 0, 800, 600, 1, 1, win)
    win.wait_for_close()

if __name__ == '__main__':
    main()
