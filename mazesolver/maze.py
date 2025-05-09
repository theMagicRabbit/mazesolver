from mazesolver import Cell
from random import seed, randrange
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
        self._break_walls_r(0, 0)

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
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        first = self._cells[0][0]
        first.has_top = False
        first.draw()

        last = self._cells[-1][-1]
        last.has_bottom = False
        last.draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            print(self._cells[i][j])
            to_visit = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j, 'left'))
            if j+1 < len(self._cells[i]) and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1, 'up'))
            if i+1 < len(self._cells) and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j, 'right'))
            if j >= 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1, 'down'))

            if not to_visit:
                self._draw_cell(i, j)
                return
            next_cell_index = randrange(0, len(to_visit), 1)

            next_i, next_j, direction = to_visit[next_cell_index] 
            match direction:
                case 'left':
                    self._cells[i][j].has_left = False
                    self._cells[next_i][next_j].has_right = False
                case 'up':
                    self._cells[i][j].has_top = False
                    self._cells[next_i][next_j].has_bottom = False
                case 'right':
                    self._cells[i][j].has_right = False
                    self._cells[next_i][next_j].has_left = False
                case 'down':
                    self._cells[i][j].has_down = False
                    self._cells[next_i][next_j].has_up = False
            self._break_walls_r(next_i, next_j)



    def __repr__(self):
        return f"Maze({self._x1}, {self._y1}, {self._num_rows}, {self._num_cols}, {self._cell_size_x}, {self._cell_size_y}, {self._win})"

