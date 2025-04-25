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
        canvas.create_line((self.p1.x, self.p1.y), (self.p2.x, self.p2.y), fill=line_color, width=2)

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

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
        line.draw(self.canvas, fill_color)
    def __repr__(self):
        return f"Window({self.width}, {self.height})"

def main():
    win = Window(800, 600)
    p1 = Point(10, 100)
    p2 = Point(10, 10)
    p3 = Point(0, 0)
    p4 = Point(800, 600)
    p5 = Point(100, 700)
    p6 = Point(17, 90)
    l1 = Line(p1, p2)
    l2 = Line(p3, p4)
    l3 = Line(p5, p6)
    win.draw_line(l1, "red")
    win.draw_line(l2, "green")
    win.draw_line(l3, "blue")
    win.wait_for_close()

if __name__ == '__main__':
    main()

