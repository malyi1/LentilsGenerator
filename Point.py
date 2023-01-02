import math


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        self.radius = Point.getFixRadius()

    def equals(self, point):
        return self.X == point.X and self.Y == point.Y

    def getRadius(self):
        return self.radius

    def getDiameter(self):
        return self.radius*2

    def shiftX(self, shift):
        self.X = shift + self.X

    def setX(self, newX):
        self.X = newX

    def isOverlapping(self, pointsInCanvas):
        for pointInCanvas in pointsInCanvas:
            if Point.isClose(self, pointInCanvas):
                return True
        return False

    def isOnCanvas(self, canvas0X, canvas0Y, canvasWidth, canvasHeight):
        if (canvas0X <= self.X <= canvas0X + canvasWidth) and (canvas0Y <= self.Y <= canvas0Y + canvasHeight):
            return True
        return False

    @staticmethod
    def getFixRadius():
        return (10 * 0.27)/2

    @staticmethod
    def getCentresDistance(point1, point2):
        return math.sqrt((point1.X - point2.X) * (point1.X - point2.X) + (point1.Y - point2.Y) * (point1.Y - point2.Y))

    # checks if points are overlapping themselves
    @staticmethod
    def isClose(point1, point2):
        return Point.getCentresDistance(point1, point2) <= point1.getDiameter()*0.75
