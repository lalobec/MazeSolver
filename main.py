from maze import Maze
from window import Window


def main():
    num_rows = 5
    num_cols = 5
    cell_size_x = 50
    cell_size_y = 50
    maze_pos_x = 20
    maze_pos_y = 20

    win = Window(800, 600)
    maze = Maze(
        maze_pos_x,
        maze_pos_y,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        0)

    win.wait_for_close()


main()
