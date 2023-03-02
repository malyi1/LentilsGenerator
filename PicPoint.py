import math

from shapely.geometry import Point


class PicPoint:
    """
        custom point class
    """

    def __init__(self, x, y, size):
        self.X = x
        self.Y = y
        self.radius = size / 2

    def equals(self, point):
        return self.X == point.X and self.Y == point.Y

    def getRadius(self):
        return self.radius

    def getDiameter(self):
        return self.radius * 2

    def shiftX(self, shift):
        self.X = shift + self.X

    def shiftY(self, shift):
        self.Y = shift + self.Y

    def setX(self, newX):
        self.X = newX

    def setY(self, newY):
        self.Y = newY

    def isOverlapping(self, pointsInCanvas):
        for pointInCanvas in pointsInCanvas:
            if PicPoint.isClose(self, pointInCanvas):
                return True
        return False

    def isOnCanvas(self, canvas):
        if canvas.contains(Point(self.X, self.Y)):
            return True
        return False

    def isInCircle(self, circleS):
        if circleS.buffer(circleS.x).contains(Point(self.X, self.Y)):
            return True
        return False

    @staticmethod
    def getCentresDistance(point1, point2):
        return math.sqrt((point1.X - point2.X) * (point1.X - point2.X) + (point1.Y - point2.Y) * (point1.Y - point2.Y))

    # checks if points are overlapping themselves
    @staticmethod
    def isClose(point1, point2):
        return PicPoint.getCentresDistance(point1, point2) <= point1.getDiameter() / 1.65  # /2 looks like intersection
