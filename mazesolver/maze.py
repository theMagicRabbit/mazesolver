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

    def _create_cells(self):
        self._cells = []
        for y in range(self._num_cols):
            row = []
            for x in range(self._num_rows):
                row.append(Cell(x, y, x + self._cell_size_x, y + self._cell_size_y, self._win))
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

