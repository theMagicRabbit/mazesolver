from tkinter import Tk, BOTH, Canvas
from mazesolver import Line

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

