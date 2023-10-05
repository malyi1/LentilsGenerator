import numpy as np
import copy
from shapely.geometry import Point, Polygon
import generator.PicPoint as pt


class PointFactory:
    """
        class holds information about canvas size, point count, point size and holds generated points
        class contains multiple methods for generation sets of points, modifying existing sets of points
    """

    def __init__(self, originX, originY, canvasWidth, canvasHeight, pointCount, pointSize):
        self.__originX = originX
        self.__originY = originY
        self.__canvasWidth = canvasWidth
        self.__canvasHeight = canvasHeight
        self.__pointCount = pointCount
        self.__pointSize = pointSize
        self.__pointList = []
        self.__canvaPointList = [Point(0, 0), Point(0, canvasHeight), Point(canvasWidth, canvasHeight),
                                 Point(canvasWidth, 0), Point(0, 0)]
        self.__canvas = Polygon(self.__canvaPointList)

    # generate random point on canvas
    def __getRandomPointOnCanvas(self):
        x = np.random.uniform(low=0, high=self.__canvasWidth)
        y = np.random.uniform(low=0, high=self.__canvasHeight)
        point = pt.PicPoint(x, y, self.__pointSize)
        return point

    # generate random point within given coordinates
    def __getRandomPoint(self, startX, startY, endX, endY):
        x = np.random.uniform(low=startX, high=endX)
        y = np.random.uniform(low=startY, high=endY)
        point = pt.PicPoint(x, y, self.__pointSize)
        return point

    # generate n not overlapping points on rectangular canvas
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

    # generate n not overlapping points for polygon
    def generateRandomPointsForPolygon(self):
        print("Generating random points for polygon...")

        # stop = points vertical span
        step = self.__canvasHeight / self.__pointCount

        # boundary height for point
        newPointHeight = self.__canvasHeight

        for i in range(self.__pointCount):
            print(newPointHeight)
            newPoint = self.__getRandomPoint(0, newPointHeight - step, self.__canvasWidth, newPointHeight)
            newPointHeight = newPoint.Y
            self.__pointList.append(newPoint)

        print("Generating random points for polygon done...")

    # generate n not overlapping points on circle
    def generateRandomPointsWithNoOverlapOnCircle(self):
        print("Generating random points...")
        for i in range(self.__pointCount ):
            positionIsCorrect = False
            while not positionIsCorrect:
                potentialPoint = self.__getRandomPointOnCanvas()
                positionIsCorrect = \
                    not potentialPoint.isOverlapping(self.__pointList) and potentialPoint.isOnCanvas(self.__canvasWidth, self.__canvasHeight)  \
                    and potentialPoint.isInCircle(Point(self.__canvasWidth, self.__canvasHeight/2))
            self.__pointList.append(potentialPoint)
        print("Generating random points done...")

    # add points to existing rectangular canvas, added points are not overlapping themselves
    def addRandomPointsWithNoOverlap(self, points, addPercentage=1):
        print("adding random points...")
        pointList = copy.deepcopy(points)
        n = int(len(pointList) * addPercentage)
        for i in range(n):
            positionIsCorrect = False
            while not positionIsCorrect:
                potentialPoint = self.__getRandomPointOnCanvas()
                positionIsCorrect = \
                    not potentialPoint.isOverlapping(pointList) \
                    and potentialPoint.isOnCanvas(self.__canvasWidth, self.__canvasHeight)
            pointList.append(potentialPoint)
        print("adding random points done...")
        return pointList

    # add points to existing circle canvas, added points are not overlapping themselves
    def addRandomPointsWithNoOverlapOnCircle(self, points, addPercentage=1):
        print("adding random points...")
        pointList = copy.deepcopy(points)
        n = int(len(pointList) * addPercentage)
        for i in range(n):
            positionIsCorrect = False
            while not positionIsCorrect:
                potentialPoint = self.__getRandomPointOnCanvas()
                positionIsCorrect = \
                    not potentialPoint.isOverlapping(pointList) and potentialPoint.isOnCanvas(self.__canvasWidth, self.__canvasHeight)  \
                    and potentialPoint.isInCircle(Point(self.__canvasWidth, self.__canvasHeight/2))
            pointList.append(potentialPoint)
        print("adding random points done...")
        return pointList

    def getPoints(self):
        return self.__pointList

    # get list of points, some of the points will be shifted in X
    # shift percentage parameter is telling method how many points will be shifted
    # rectangular canvas
    def getShiftedXPointsList(self, points, maxShift, shiftPercentage=1):
        print("shifting X of random points...")
        pointList = copy.deepcopy(points)
        k = int(len(pointList) * shiftPercentage)
        pointsToShift = np.random.choice(pointList, k, replace=False)
        for pointToShift in pointsToShift:
            positionIsCorrect = False
            checkPoint = copy.deepcopy(pointToShift)
            while not positionIsCorrect:
                randomOffset = np.random.uniform(low=-maxShift, high=maxShift, size=1)
                checkPoint.setX(pointToShift.X + randomOffset)
                positionIsCorrect = \
                    not checkPoint.isOverlapping(pointList) \
                    and checkPoint.isOnCanvas(self.__canvasWidth, self.__canvasHeight)
            pointToShift.X = checkPoint.X
        print("shifting X of random points done...")
        return pointList

    # get list of points, some of the points will be shifted in X and Y
    # shift percentage parameter is telling method how many points will be shifted
    # rectangular canvas
    def getShiftedXYPointsList(self, points, maxShift, shiftPercentage=1):
        print("shifting X and Y of random points...")
        pointList = copy.deepcopy(points)
        k = int(len(pointList) * shiftPercentage)
        pointsToShift = np.random.choice(pointList, k, replace=False)
        for pointToShift in pointsToShift:
            positionIsCorrect = False
            checkPoint = copy.deepcopy(pointToShift)
            while not positionIsCorrect:
                randomOffsetX = np.random.uniform(low=-maxShift, high=maxShift)
                randomOffsetY = np.random.uniform(low=-maxShift, high=maxShift)
                checkPoint.setX(pointToShift.X + randomOffsetX)
                checkPoint.setY(pointToShift.Y + randomOffsetY)
                positionIsCorrect = \
                    not checkPoint.isOverlapping(pointList) \
                    and checkPoint.isOnCanvas(self.__canvasWidth, self.__canvasHeight)
            pointToShift.X = checkPoint.X
            pointToShift.Y = checkPoint.Y
        print("shifting X and Y of random points done...")
        return pointList

    # get list of points, some of the points will be shifted in X and Y
    # shift percentage parameter is telling method how many points will be shifted
    # circle canvas
    def getShiftedXYPointsListOnCircle(self, points, maxShift, shiftPercentage=1):
        print("shifting X and Y of random points...")
        pointList = copy.deepcopy(points)
        k = int(len(pointList) * shiftPercentage)
        pointsToShift = np.random.choice(pointList, k, replace=False)
        for pointToShift in pointsToShift:
            positionIsCorrect = False
            checkPoint = copy.deepcopy(pointToShift)
            while not positionIsCorrect:
                randomOffsetX = np.random.uniform(low=-maxShift, high=maxShift, size=1)
                randomOffsetY = np.random.uniform(low=-maxShift, high=maxShift, size=1)
                checkPoint.setX(pointToShift.X + randomOffsetX)
                checkPoint.setY(pointToShift.Y + randomOffsetY)
                positionIsCorrect = \
                    not checkPoint.isOverlapping(pointList) and checkPoint.isOnCanvas(self.__canvasWidth, self.__canvasHeight) \
                    and checkPoint.isInCircle(Point(self.__canvasWidth, self.__canvasHeight/2))
            pointToShift.X = checkPoint.X
            pointToShift.Y = checkPoint.Y
        print("shifting X and Y of random points done...")
        return pointList

    # get list of points, some of the points will be removed
    # remove percentage parameter is telling method how many points will be removed
    def removePoints(self, points, removePercentage=1):
        print("removing random points...")
        pointList = copy.deepcopy(points)
        k = int(len(pointList) * removePercentage)
        pointsToRemove = np.random.choice(pointList, k, replace=False)
        for pointToRemove in pointsToRemove:
            pointList.remove(pointToRemove)
        print("removing random points done...")
        return pointList

    # generate symmetric half to right side of the original
    @staticmethod
    def getSymmetricHalf(pointFactory):
        print("copying symmetric half...")
        symmetricHalfFactory = copy.deepcopy(pointFactory)
        for point in symmetricHalfFactory.__pointList:
            point.X = (2 * pointFactory.__canvasWidth) - point.X
        print("copying symmetric half done...")
        return symmetricHalfFactory



