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
        random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
        print(f"Creating a new cell at {i}, {j}")
        cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        cells_to_visit = []
        while True:
            if i > 0 and self._cells[i-1][j].visited is False:
                cells_to_visit.append((i-1, j))
            if i < self._num_rows-1 and self._cells[i+1][j].visited is False:
                cells_to_visit.append((i+1, j))
            if j > 0 and self._cells[i][j-1].visited is False:
                cells_to_visit.append((i, j-1))
            if j < self._num_cols-1 and self._cells[i][j+1].visited is False:
                cells_to_visit.append((i, j+1))
            if cells_to_visit == []:
                self._draw_cell(i, j)
                return
            next_cell = random.choice(cells_to_visit)
            if next_cell[0] == i:
                if next_cell[1] == j-1:
                    self._cells[i][j-1].has_right_wall = False
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i, j-1)
                    self._draw_cell(i, j)
                    self._break_walls_r(i, j-1)
                else:
                    self._cells[i][j+1].has_left_wall = False
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i, j+1)
                    self._draw_cell(i, j)
                    self._break_walls_r(i, j+1)
            elif next_cell[1] == j:
                if next_cell[0] == i-1:
                    self._cells[i-1][j].has_bottom_wall = False
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i-1, j)
                    self._draw_cell(i, j)
                    self._break_walls_r(i-1, j)
                else:
                    self._cells[i+1][j].has_top_wall = False
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i+1, j)
                    self._draw_cell(i, j)
                    self._break_walls_r(i+1, j)






