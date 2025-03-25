from tkinter import BOTH, Canvas, Tk
from lines import Point, Line
from cell import Cell

# Window class


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color=fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False


def main():
    win = Window(800, 600)

    pointA_1 = Point(1, 1)
    pointB_1 = Point(70, 70)
    line1 = Line(pointA_1, pointB_1)

    pointA_2 = Point(55, 43)
    pointB_2 = Point(236, 70)
    line2 = Line(pointA_2, pointB_2)

    cell1 = Cell(100, 300, 450, 550, win)
    cell1.draw()
    cell2 = Cell(150, 350, 350, 450, win)
    cell2.draw()
    cell3 = Cell(100, 300, 450, 550, win)
    cell3.draw()

    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()


main()
