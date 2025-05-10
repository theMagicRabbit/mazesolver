from mazesolver import Cell
from random import seed, randrange
from time import sleep


class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, maze_seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if maze_seed:
            seed(maze_seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)
        if not self._win:
            return
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._win:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win:
            self._win.redraw()
        sleep(0.03)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j, 'left'))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1, 'down'))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j, 'right'))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1, 'up'))

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
                    self._cells[i][j].has_bottom = False
                    self._cells[next_i][next_j].has_top = False
            print(i, j, str(self._cells[i][j]), direction, next_i, next_j, str(self._cells[next_i][next_j]))
            self._break_walls_r(next_i, next_j)



    def __repr__(self):
        return f"Maze({self._x1}, {self._y1}, {self._num_rows}, {self._num_cols}, {self._cell_size_x}, {self._cell_size_y}, {self._win})"

