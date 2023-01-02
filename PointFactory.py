import numpy as np
import copy
import Point as pt


class PointFactory:

    def __init__(self, originX, originY, canvWidth, canvHeight, pointCount):
        self.__originX = originX
        self.__originY = originY
        self.__canvasWidth = canvWidth
        self.__canvasHeight = canvHeight
        self.__pointCount = pointCount
        self.__pointList = []

# generate random point on canvas
    def __getRandomPointOnCanvas(self):
        x = np.random.uniform(low=0, high=self.__canvasWidth, size=1)
        y = np.random.uniform(low=0, high=self.__canvasHeight, size=1)
        point = pt.Point(x[0], y[0])
        return point

# generate n points which are not overlapping themselves
    def generateRandomPointsWithNoOverlap(self):
        print("Generating random points...")
        self.__pointList.append(self.__getRandomPointOnCanvas())

        for i in range(self.__pointCount - 1):
            positionIsCorrect = False
            while not positionIsCorrect:
                potentialPoint = self.__getRandomPointOnCanvas()
                positionIsCorrect = not potentialPoint.isOverlapping(self.__pointList)
            self.__pointList.append(potentialPoint)
        print("Generating random points done...")

# add points to existing canvas wih points which are not overlapping themselves
    def addRandomPointsWithNoOverlap(self, n):
        print("adding random points...")
        for i in range(n):
            positionIsCorrect = False
            while not positionIsCorrect:
                potentialPoint = self.__getRandomPointOnCanvas()
                positionIsCorrect = not potentialPoint.isOverlapping(self.__pointList)
            self.__pointList.append(potentialPoint)

    def getPoints(self):
        return self.__pointList

    def getShiftedPointsList(self, maxShift, shiftPercentage=1):
        k = int(len(self.__pointList) * shiftPercentage)
        pointList = copy.deepcopy(self.__pointList)
        pointsToShift = np.random.choice(pointList, k, replace=False)
        for pointToShift in pointsToShift:
            positionIsCorrect = False
            checkPoint = copy.deepcopy(pointToShift)
            while not positionIsCorrect:
                randomOffset = np.random.uniform(low=-maxShift, high=maxShift, size=1)
                checkPoint.setX(pointToShift.X + randomOffset)
                positionIsCorrect = \
                    not checkPoint.isOverlapping(pointList) \
                    and checkPoint.isOnCanvas(self.__originX, self.__originY, self.__canvasWidth, self.__canvasHeight)
            pointToShift.X = checkPoint.X
        return pointList

    # generate symmetric half to right side of the original
    @staticmethod
    def getSymmetricHalf(pointFactory):
        symmetricHalfFactory = copy.deepcopy(pointFactory)

        for point in symmetricHalfFactory.__pointList:
            point.X = (2 * pointFactory.__canvasWidth) - point.X

        return symmetricHalfFactory

    # generate random point on specified part of the canvas
    @staticmethod
    def __getRandomSpecifiedPoint(startX, startY, endX, endY):
        x = np.random.uniform(low=startX, high=endX, size=1)
        y = np.random.uniform(low=startY, high=endY, size=1)
        point = pt.Point(x[0], y[0])
        return point

    # checks if points are overlaping themselves
    @staticmethod
    def isClose(point1, point2):
        return pt.Point.getCentresDistance(point1, point2) <= point1.getRadius()



