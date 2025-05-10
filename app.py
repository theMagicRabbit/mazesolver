from mazesolver import Window, Maze
from math import floor

def main():
    num_cols = 16
    num_rows = 12
    x = 800
    y = 600
    margin = 50
    cell_size_x = (x - 2 * margin) / num_cols
    cell_size_y = (y - 2 * margin) / num_rows
    win = Window(x, y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    win.wait_for_close()

if __name__ == '__main__':
    main()
