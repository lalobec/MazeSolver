class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, pointA, pointB):
        self.__pointA = pointA
        self.__pointB = pointB

    def draw(self, Canvas, fill_color):
        Canvas.create_line(self.__pointA.x, self.__pointA.y, self.__pointB.x, self.__pointB.y, fill=fill_color, width=2)
