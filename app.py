from mazesolver import Window, Maze
from math import floor

def main():
    x = 802
    y = 602
    cell_size = 25
    rows = floor(800 / cell_size)
    cols = floor(600 / cell_size)
    win = Window(x, y)
    maze = Maze(1, 1, rows, cols, cell_size, cell_size, win)
    win.wait_for_close()

if __name__ == '__main__':
    main()
