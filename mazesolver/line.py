from tkinter import Canvas
from mazesolver import Point

class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, line_color: str):
        canvas.create_line((self.p1.x, self.p1.y), (self.p2.x, self.p2.y), fill=line_color, width=16)

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"

