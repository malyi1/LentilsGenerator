import PointFactory
import PicFactory


class DataGenerator:

    # string export
    # first row = point count then points coordinates in format [x y] follows
    @staticmethod
    def getStringForExport(pointsList):
        stringToExport = str(len(pointsList)) + "\n"
        for point in pointsList:
            stringToExport += str(point.X) + ", " + str(point.Y) + "\n"
        return stringToExport


if __name__ == "__main__":

    pixel = 0.27
    width = 200 * pixel
    height = 200 * pixel
    shiftedList = []

    nrOfPoints = 80
    nrOfChangedSizePoints = 0
    sizeOfPoints = 10 * pixel

    listOfPoints = []
    symmetricPoints = []
    setCount = 1

    for setNum in range(setCount):

        # files
        picSuffix = ".png"
        fileSuffix = ".txt"

        # rect canvas with original points set
        originalCanvasFactoryR = PointFactory.PointFactory(0, 0, width / 2, height, nrOfPoints, sizeOfPoints)
        originalCanvasFactoryR.generateRandomPointsWithNoOverlap()
        symmetricCanvasFactoryR = originalCanvasFactoryR.getSymmetricHalf(originalCanvasFactoryR)

        # circ canvas with original points set
        originalCanvasFactoryC = PointFactory.PointFactory(0, 0, width / 2, height, nrOfPoints, sizeOfPoints)
        originalCanvasFactoryC.generateRandomPointsWithNoOverlapOnCircle()
        symmetricCanvasFactoryC = originalCanvasFactoryC.getSymmetricHalf(originalCanvasFactoryC)

        # rect original plotter
        plotterOriginal = PicFactory.PicFactory(width, height, pixel, "img/100px/set" + str(setNum) + "_original.png")

        # original points (rectangular canvas)*************************************************************************
        pointList = originalCanvasFactoryR.getPoints() + symmetricCanvasFactoryR.getPoints()
        plotterOriginal.drawPoints(pointList)
        with open("img/100px/set" + " original rect" + fileSuffix, 'w') as f:
            f.write(DataGenerator.getStringForExport(pointList))

        # circ original plotter
        plotterOriginalC = PicFactory.PicFactory(width, height, pixel, "img/100px/set" + str(setNum) + "_originalCircle.png")
        
        # original points (circular canvas)****************************************************************************
        pointList = originalCanvasFactoryC.getPoints() + symmetricCanvasFactoryC.getPoints()
        plotterOriginalC.drawPoints(pointList)
        with open("img/100px/set" + " original circ" + fileSuffix, 'w') as f:
            f.write(DataGenerator.getStringForExport(pointList))

        # polygon plotting
        polygonCanvasFactory = PointFactory.PointFactory(0, 0, width / 2, height, nrOfPoints, sizeOfPoints)
        polygonCanvasFactory.generateRandomPointsForPolygon()
        symmetricPolygonCanvasFactory = polygonCanvasFactory.getSymmetricHalf(polygonCanvasFactory)
        polygonPlotter = PicFactory.PicFactory(width, height, pixel, "img/100px/set" + str(setNum) + "_polygon.png")
        polygonPlotter.drawSymmetricPolygon(polygonCanvasFactory.getPoints(), symmetricPolygonCanvasFactory.getPoints())

        for index in range(1):

            # describe how many points from original dataset will be changed
            deformationPercentage = (index + 1) * 0.1

            # point shift in XY (rectangular canvas)*******************************************************************
            fileName = "img/100px/set" + str(setNum) + " shiftXY=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryR.getShiftedXYPointsList(originalCanvasFactoryR.getPoints(),
                                                                              maxShift=width * 0.4,
                                                                              shiftPercentage=deformationPercentage) + symmetricCanvasFactoryR.getPoints()
            plotterShiftedXY = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                                     fileName=fileName + picSuffix)
            plotterShiftedXY.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # point shift in XY (circle canvas)************************************************************************
            fileName = "img/100px/setC" + str(setNum) + " shiftXYCircle=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryC.getShiftedXYPointsList(originalCanvasFactoryC.getPoints(),
                                                                              maxShift=width * 0.4,
                                                                              shiftPercentage=deformationPercentage) + symmetricCanvasFactoryC.getPoints()
            plotterShiftedXYC = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                                      fileName=fileName + picSuffix)
            plotterShiftedXYC.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # add points / no shift (rectangular canvas)***************************************************************
            fileName = "img/100px/set" + str(setNum) + " add=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryR.addRandomPointsWithNoOverlap(originalCanvasFactoryR.getPoints(),
                                                                                    deformationPercentage) + symmetricCanvasFactoryR.getPoints()
            plotterAdd = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                               fileName=fileName + picSuffix)
            plotterAdd.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # add points / no shift (circle canvas)********************************************************************
            fileName = "img/100px/setC" + str(setNum) + " addCircle=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryC.addRandomPointsWithNoOverlap(originalCanvasFactoryC.getPoints(),
                                                                                    deformationPercentage) + symmetricCanvasFactoryC.getPoints()
            plotterAddC = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                                fileName=fileName + picSuffix)
            plotterAddC.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # add points / shift (rectangular canvas)******************************************************************
            fileName = "img/100px/set" + str(setNum) + " add + shift XY=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryR.addRandomPointsWithNoOverlap(
                originalCanvasFactoryR.getShiftedXYPointsList(originalCanvasFactoryR.getPoints(), maxShift=width * 0.4,
                                                              shiftPercentage=deformationPercentage),
                deformationPercentage) + symmetricCanvasFactoryR.getPoints()
            plotterAdd = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                               fileName=fileName + picSuffix)
            plotterAdd.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # add points / shift (circle canvas)***********************************************************************
            fileName = "img/100px/setC" + str(setNum) + " addCircle + shift XY=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryC.addRandomPointsWithNoOverlap(
                originalCanvasFactoryC.getShiftedXYPointsList(originalCanvasFactoryC.getPoints(), maxShift=width * 0.4,
                                                              shiftPercentage=deformationPercentage),
                deformationPercentage) + symmetricCanvasFactoryC.getPoints()
            plotterAddC = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                                fileName=fileName + picSuffix)
            plotterAddC.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # remove points (rectangular canvas)***********************************************************************
            fileName = "img/100px/set" + str(setNum) + " remove=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryR.removePoints(originalCanvasFactoryR.getPoints(),
                                                                    deformationPercentage) + symmetricCanvasFactoryR.getPoints()
            plotterRemove = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                                  fileName=fileName + picSuffix)
            plotterRemove.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))

            # remove points (circle canvas)****************************************************************************
            fileName = "img/100px/setC" + str(setNum) + " removeCircle=" + str(deformationPercentage)
            modifiedPointList = originalCanvasFactoryC.removePoints(originalCanvasFactoryC.getPoints(),
                                                                    deformationPercentage) + symmetricCanvasFactoryC.getPoints()
            plotterRemoveC = PicFactory.PicFactory(width=width, height=height, pixelSize=pixel,
                                                   fileName=fileName + picSuffix)
            plotterRemoveC.drawPoints(modifiedPointList)
            with open(fileName + fileSuffix, 'w') as f:
                f.write(DataGenerator.getStringForExport(modifiedPointList))
