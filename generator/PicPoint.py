import math

from shapely.geometry import Point
from math import sqrt


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

    def isOnCanvas(self, width, height):
        # if canvas.contains(Point(self.X, self.Y)):
        #     return True
        # return False
        # Check if the circle with center at the point and given diameter is within the canvas bounds
        if self.X - self.getRadius() < 0 or self.X + self.getRadius() > width:
            return False
        if self.Y - self.getRadius() < 0 or self.Y + self.getRadius() > height:
            return False
        return True

    def isInCircle(self, circleS):
        # if circleS.buffer(circleS.x).contains(Point(self.X, self.Y)):
        #     return True
        # return False
        distance = sqrt((self.X - circleS.x)**2 + (self.Y - circleS.y)**2)
        circleRadius = circleS.x

        inCircleWithBorder = distance <= (circleRadius - self.getDiameter())

        fromLine = abs(circleS.x - self.X) > self.getDiameter()

        # if distance + self.getRadius() < circleS.y and self.X >= self.getRadius() and self.X < circleS.x - self.getRadius() and self.Y > self.getRadius() and self.Y < circleS.y*2 - self.getRadius():
        if inCircleWithBorder and fromLine:
            return True
        return False


    @staticmethod
    def getCentresDistance(point1, point2):
        return math.sqrt((point1.X - point2.X)**2 + (point1.Y - point2.Y)**2)

    # checks if points are overlapping themselves
    @staticmethod
    def isClose(point1, point2):
        return PicPoint.getCentresDistance(point1, point2) <= point1.getDiameter() * 1.5 #/ 1.25  # /2 looks like intersection
