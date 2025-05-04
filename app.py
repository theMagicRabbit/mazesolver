from mazesolver import Window, Maze

def main():
    win = Window(800, 600)
    maze = Maze(0, 0, 800, 600, 1, 1, win)
    win.wait_for_close()

if __name__ == '__main__':
    main()
