import generator.PointFactory as PointFactory
import generator.PicFactory as PicFactory


class DataGenerator:
    """
        class for generating sets of pictures with defined deformations
        for each picture a txt file with coordinations is generated
    """
    # string export
    # first row = point count then points coordinates in format [x y] follows
    @staticmethod
    def getStringForExport(pointsList):
        stringToExport = str(len(pointsList)) + "\n"
        for point in pointsList:
            stringToExport += str(point.X) + ", " + str(point.Y) + "\n"
        return stringToExport

    def generateOriginalSet(width, height, nrOfPoints, sizeOfPoints):
        # rect canvas with original points set
        originalCanvasFactoryR = PointFactory.PointFactory(0, 0, width / 2, height, nrOfPoints, sizeOfPoints)
        originalCanvasFactoryR.generateRandomPointsWithNoOverlap()
        symmetricCanvasFactoryR = originalCanvasFactoryR.getSymmetricHalf(originalCanvasFactoryR)

        # circ canvas with original points set
        originalCanvasFactoryC = PointFactory.PointFactory(0, 0, width / 2, height, nrOfPoints, sizeOfPoints)
        originalCanvasFactoryC.generateRandomPointsWithNoOverlapOnCircle()
        symmetricCanvasFactoryC = originalCanvasFactoryC.getSymmetricHalf(originalCanvasFactoryC)

        return [originalCanvasFactoryR, originalCanvasFactoryC, symmetricCanvasFactoryR, symmetricCanvasFactoryC]

    def generateLentils(width, height, nrOfPoints, sizeOfPoints, setCount, sigma, canvasWidth, canvasHeight, maxShift, backgroundColor, foregroundColor, pointColor):
        for setNum in range(setCount):
            # files
            picSuffix = ".png"
            fileSuffix = ".txt"

            # range defines percentage deformation --> 0, 20, 40, 60, 80, 100 %
            for index in range(6):
                # describe how many points from original dataset will be changed
                deformationPercentage = round((index) * 0.2, 1)

                # generate new original set before deformation
                originalCanvasFactoryR, originalCanvasFactoryC, symmetricCanvasFactoryR, symmetricCanvasFactoryC = DataGenerator.generateOriginalSet(
                    width, height, nrOfPoints, sizeOfPoints)

                # # point shift in XY (rectangular canvas)*******************************************************************
                # fileName = "img/set" + str(setNum) + " shiftXY=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryR.getShiftedXYPointsList(originalCanvasFactoryR.getPoints(),
                #                                                                   maxShift=width * 0.4,
                #                                                                   shiftPercentage=deformationPercentage) + symmetricCanvasFactoryR.getPoints()
                # plotterShiftedXY = PicFactory.PicFactory(width=width, height=height,
                #                                          fileName=fileName + picSuffix)
                # plotterShiftedXY.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))

                # point shift in XY (circle canvas)************************************************************************
                fileName = "img/" + str(int(round((1-deformationPercentage)*100,0))) + "set" + str(setNum)
                modifiedPointList = originalCanvasFactoryC.getShiftedXYPointsListOnCircle(originalCanvasFactoryC.getPoints(),
                                                                                  maxShift= maxShift, # width * 0.5, # sizeOfPoints * 2, # width * 0.1, # width * 0.4
                                                                                  shiftPercentage=deformationPercentage) + symmetricCanvasFactoryC.getPoints()
                plotterShiftedXYC = PicFactory.PicFactory(
                    width=width,
                    height=height,
                    fileName=fileName + picSuffix,
                    pointDiameter=sizeOfPoints,
                    sigma=sigma,
                    canvasWidth=canvasWidth,
                    canvasHeight=canvasHeight,
                    backgroundColor=backgroundColor,
                    foregroundColor=foregroundColor,
                    pointColor=pointColor
                )
                plotterShiftedXYC.drawPoints(modifiedPointList)
                with open(fileName + fileSuffix, 'w') as f:
                    f.write(DataGenerator.getStringForExport(modifiedPointList))

                # # generate new original set before deformation
                # originalCanvasFactoryR, originalCanvasFactoryC, symmetricCanvasFactoryR, symmetricCanvasFactoryC = DataGenerator.generateOriginalSet(
                #     width, height, nrOfPoints, sizeOfPoints)

                # # add points / no shift (rectangular canvas)***************************************************************
                # fileName = "img/set" + str(setNum) + " add=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryR.addRandomPointsWithNoOverlap(
                #     originalCanvasFactoryR.getPoints(),
                #     deformationPercentage) + symmetricCanvasFactoryR.getPoints()
                # plotterAdd = PicFactory.PicFactory(width=width, height=height,
                #                                    fileName=fileName + picSuffix)
                # plotterAdd.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))

                # # add points / no shift (circle canvas)********************************************************************
                # fileName = "img/setC" + str(setNum) + " addCircle=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryC.addRandomPointsWithNoOverlap(
                #     originalCanvasFactoryC.getPoints(),
                #     deformationPercentage) + symmetricCanvasFactoryC.getPoints()
                # plotterAddC = PicFactory.PicFactory(width=width, height=height,
                #                                     fileName=fileName + picSuffix)
                # plotterAddC.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))

                # # generate new original set before deformation
                # originalCanvasFactoryR, originalCanvasFactoryC, symmetricCanvasFactoryR, symmetricCanvasFactoryC = DataGenerator.generateOriginalSet(
                #     width, height, nrOfPoints, sizeOfPoints)

                # # add points / shift (rectangular canvas)******************************************************************
                # fileName = "img/set" + str(setNum) + " add + shift XY=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryR.addRandomPointsWithNoOverlap(
                #     originalCanvasFactoryR.getShiftedXYPointsList(originalCanvasFactoryR.getPoints(),
                #                                                   maxShift=width * 0.4,
                #                                                   shiftPercentage=deformationPercentage),
                #     deformationPercentage) + symmetricCanvasFactoryR.getPoints()
                # plotterAdd = PicFactory.PicFactory(width=width, height=height,
                #                                    fileName=fileName + picSuffix)
                # plotterAdd.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))

                # # add points / shift (circle canvas)***********************************************************************
                # fileName = "img/setC" + str(setNum) + " addCircle + shift XY=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryC.addRandomPointsWithNoOverlap(
                #     originalCanvasFactoryC.getShiftedXYPointsList(originalCanvasFactoryC.getPoints(),
                #                                                   maxShift=width * 0.4,
                #                                                   shiftPercentage=deformationPercentage),
                #     deformationPercentage) + symmetricCanvasFactoryC.getPoints()
                # plotterAddC = PicFactory.PicFactory(width=width, height=height,
                #                                     fileName=fileName + picSuffix)
                # plotterAddC.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))

                # # generate new original set before deformation
                # originalCanvasFactoryR, originalCanvasFactoryC, symmetricCanvasFactoryR, symmetricCanvasFactoryC = DataGenerator.generateOriginalSet(
                #     width, height, nrOfPoints, sizeOfPoints)

                # # remove points (rectangular canvas)***********************************************************************
                # fileName = "img/set" + str(setNum) + " remove=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryR.removePoints(originalCanvasFactoryR.getPoints(),
                #                                                         deformationPercentage) + symmetricCanvasFactoryR.getPoints()
                # plotterRemove = PicFactory.PicFactory(width=width, height=height,
                #                                       fileName=fileName + picSuffix)
                # plotterRemove.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))

                # # remove points (circle canvas)****************************************************************************
                # fileName = "img/setC" + str(setNum) + " removeCircle=" + str(deformationPercentage)
                # modifiedPointList = originalCanvasFactoryC.removePoints(originalCanvasFactoryC.getPoints(),
                #                                                         deformationPercentage) + symmetricCanvasFactoryC.getPoints()
                # plotterRemoveC = PicFactory.PicFactory(width=width, height=height,
                #                                        fileName=fileName + picSuffix)
                # plotterRemoveC.drawPoints(modifiedPointList)
                # with open(fileName + fileSuffix, 'w') as f:
                #     f.write(DataGenerator.getStringForExport(modifiedPointList))
        print("Generating done...")


if __name__ == "__main__":
    # this width and height specifies the grid, where points will be generated
    width = 200
    height = 200

    nrOfPoints = 80             # how many point should be generated on left half
    sizeOfPoints = 5 #10 # * 0.2     # how big should be the point
    setCount = 3               # how many datasets should be generated

    # listOfPoints = []
    # symmetricPoints = []
    # shiftedList = []

    # for testing only
    # DataGenerator.generateLentilsFromOriginal(width, height, nrOfPoints, sizeOfPoints, setCount)

    DataGenerator.generateLentils(width, height, nrOfPoints, sizeOfPoints, setCount)

    # # PART 2:  polygon plotting
    # polygonCanvasFactory = PointFactory.PointFactory(0, 0, width / 2, height, nrOfPoints, sizeOfPoints)
    # polygonCanvasFactory.generateRandomPointsForPolygon()
    # symmetricPolygonCanvasFactory = polygonCanvasFactory.getSymmetricHalf(polygonCanvasFactory)
    # polygonPlotter = PicFactory.PicFactory(width, height, "img/set" + str(setNum) + "_polygon.png")
    # polygonPlotter.drawSymmetricPolygon(polygonCanvasFactory.getPoints(), symmetricPolygonCanvasFactory.getPoints())





















