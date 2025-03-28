from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
            ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                cell = Cell(self._win)
                row.append(cell)
            self._cells.append(row)

        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._win:
            return
        cell_x1 = self._x1 + (i*self._cell_size_x)
        cell_x2 = cell_x1 + self._cell_size_x
        cell_y1 = self._y1 + (j*self._cell_size_y)
        cell_y2 = cell_y1 + self._cell_size_y

        cell = self._cells[i][j]
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            cells_to_visit = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < self._num_rows and 0 <= nj < self._num_cols:
                    if not self._cells[ni][nj].visited:
                        cells_to_visit.append((ni, nj, di, dj))
            if cells_to_visit == []:
                self._draw_cell(i, j)
                return
            ni, nj, di, dj = random.choice(cells_to_visit)
            direction_map = {
                (0, -1): ("has_top_wall", "has_bottom_wall"),
                (0, 1): ("has_bottom_wall", "has_top_wall"),
                (-1, 0): ("has_left_wall", "has_right_wall"),
                (1, 0): ("has_right_wall", "has_left_wall")
            }

            current_wall, neighbor_wall = direction_map[(di, dj)]
            setattr(self._cells[i][j], current_wall, False)
            setattr(self._cells[ni][nj], neighbor_wall, False)
            self._break_walls_r(ni, nj)

    def _reset_cells_visited(self):
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._cells[i][j].visited = False

    def solve(self):
        if self._solve_r(0, 0):
            return True
        return False

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_rows-1 and j == self._num_cols-1:
            return True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        direction_map = {
                (0, -1): ("has_top_wall", "has_bottom_wall"),
                (0, 1): ("has_bottom_wall", "has_top_wall"),
                (-1, 0): ("has_left_wall", "has_right_wall"),
                (1, 0): ("has_right_wall", "has_left_wall")
            }
        for di, dj in directions:
            current_wall, neighbor_wall = direction_map[(di, dj)]
            ni, nj = i + di, j + dj
            if 0 <= ni < self._num_rows and 0 <= nj < self._num_cols:
                if (getattr(self._cells[i][j], current_wall) is False
                        and getattr(self._cells[ni][nj], neighbor_wall) is False
                        and self._cells[ni][nj].visited is False):
                    self._cells[i][j].draw_move(self._cells[ni][nj])
                    if self._solve_r(ni, nj):
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[ni][nj], undo=True)
        return False
