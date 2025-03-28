import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_2(self):
        num_cols = 8
        num_rows = 7
        m1 = Maze(0, 0, num_rows, num_cols, 6, 6)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_3(self):
        num_cols = 18
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_break(self):
        num_rows = 5
        num_cols = 5
        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_rows-1][num_cols-1].has_bottom_wall,
                         False)

    def test_maze_visited_cells(self):
        num_rows = 5
        num_cols = 5
        m1 = Maze(0, 0, num_rows, num_cols, 50, 50)
        for i in range(num_rows):
            for j in range(num_cols):
                self.assertEqual(m1._cells[i][j].visited, False)


if __name__ == "__main__":
    unittest.main()
