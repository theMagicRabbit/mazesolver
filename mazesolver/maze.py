from mazesolver import Cell
from random import seed
from time import sleep

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row = []
            dx = self._cell_size_x * i
            current_i = self._x1 + dx
            for j in range(self._num_cols):
                dy = self._cell_size_y * j
                current_j = self._y1 + dy
                row.append(Cell(current_i, current_j, current_i + self._cell_size_x, current_j + self._cell_size_y, self._win))
            self._cells.append(row)
        if self._win:
            for i in range(len(self._cells)):
                for j in range(len(self._cells[i])):
                    self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        print(self._cells[i][j])
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        first = self._cells[0][0]
        first.has_top = False
        first.draw()

        last = self._cells[-1][-1]
        last.has_bottom = False
        last.draw()

    def _break_walls_r(self, i, j):
        pass
        self.visited = True
        while True:
            to_visit = []
            



    def __repr__(self):
        return f"Maze({self._x1}, {self._y1}, {self._num_rows}, {self._num_cols}, {self._cell_size_x}, {self._cell_size_y}, {self._win})"

