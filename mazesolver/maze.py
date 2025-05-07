from mazesolver import Cell

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
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = []
        for y in range(self._num_cols):
            row = []
            dy = self._cell_size_y * y
            current_y = self._y1 + dy
            for x in range(self._num_rows):
                dx = self._cell_size_x * x
                current_x = self._x1 + dx
                row.append(Cell(current_x, current_y, current_x + self._cell_size_x, current_y + self._cell_size_y, self._win))
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

    def _break_entrance_and_exit(self):
        first = self._cells[0][0]
        first.has_top = False
        first.draw()

        last = self._cells[-1][-1]
        last.has_bottom = False
        last.draw()


    def __repr__(self):
        return f"Maze({self._x1}, {self._y1}, {self._num_rows}, {self._num_cols}, {self._cell_size_x}, {self._cell_size_y}, {self._win})"

