import math
import numpy as np
import PointFactory
import PicFactory
from matplotlib import pyplot as plt


class DataGenerator:
    # These fields are used for some types of noise application
    minRangeX = 0
    maxRangeX = 0
    minRangeY = 0
    maxRangeY = 0
    pixel = 0.27 # mm


    @staticmethod
    def generateRandomPoints(canvasWidth, canvasHeight, n):
        print("Generating random points...")
        # width and height are size of canvas, we will generate points only in one half of X axes
        width = int(canvasWidth / 2)
        height = int(canvasHeight)
        ptList = []
        radius = 10 * pixel
        # pro zlaty rez: potreba 2/3 --> pulku tretiny od krajů
        # zlatawidth = width /6
        # zlataheight = height/6

        # pridam prvni bod
        ptList.append(DataGenerator.randPoint(0, 0, width, height))

        for i in range(n-1):

            isClose = True

            while isClose:

                point = DataGenerator.randPoint(0, 0, width, height)

                for pt in ptList:

                    distance = math.sqrt((point.X - pt.X) * (point.X - pt.X) + (point.Y - pt.Y) * (point.Y - pt.Y))
                    isClose = distance <= radius

                    if isClose:
                        break

            ptList.append(point)

        return ptList

    @staticmethod
    def addRandomPoints(canvasWidth, canvasHeight, n, point_list):
        print("Generating random points...")
        # width and height are size of canvas, we will generate points only in one half of X axes
        width = int(canvasWidth / 2)
        height = int(canvasHeight)
        ptList = point_list
        radius = 10 * pixel

        for i in range(n):
            isClose = True
            while isClose:
                new_point = DataGenerator.randPoint(0, 0, width, height)
                for pt in ptList:
                    distance = math.sqrt((new_point.X - pt.X) * (new_point.X - pt.X) + (new_point.Y - pt.Y) * (new_point.Y - pt.Y))
                    isClose = distance <= radius
                    if isClose:
                        break

            ptList.append(new_point)

        return ptList

    @staticmethod
    def randPoint(startX, startY, endX, endY):
        x = np.random.uniform(low=startX, high=endX, size=1)
        y = np.random.uniform(low=startY, high=endY, size=1)
        new_point = Point(x[0], y[0])
        return new_point

    @staticmethod
    def shiftX(points, width, maxShift, shiftPercentage=1):
        # posunu body na ose x o rand kousek, nesmí přesáhnout osu symetrie !
        #  prozatím posouvám min o 5px a max o 1/4 šířky, v momentě, kdy jsem za 1/4 a přičetla bych čtvrtinu
        #  dostanu se přes osu symetrie -> nebudu odečítat,ale přičítat
        # to samé nutno dodělat na opačnou stranu (když bych šla do mínusu
        #  -> dořešíme v závislosti na velikosti plátna
        axis = width / 2
        shiftPoints = []

        # pouze určité procento bodů bude posunuto
        sh_points = int(len(points) * shiftPercentage)
        counter = len(points)
        # delitel = counter / sh_points
        count = 0
        for p in points:
            if counter <= sh_points:
                # maxshift udává pás šířky, o ktrerý max můžer být proveden posun na ose x (v jedné polovině)
                randPosun = np.random.uniform(low=5*pixel, high=width/2 * maxShift, size=1)
                count += 1
                # random shift direction - 0 - 0.5 posun vlevo na x; > 0.5 doprava na x
                dir = np.random.rand(1)

                if dir > 0.5:
                    newX = p.X + randPosun[0]
                    # Přičítám randNr -> hrozí, že přejdu přes osu symetrie
                    # to, o co přelezu axis, tak o tolik to od axis posunu zpět na správnou půlku

                    if newX >= axis:
                        rozdil = axis - newX
                        newX = axis - abs(rozdil)
                else:
                    newX = p.X - randPosun[0]
                    # Odečítám randNr -> hrozí, že přejdu do mínusu (mimo plátno)
                    if newX <= 0:
                        rozdil = 0 - newX
                        newX = rozdil

                shiftPoint = Point(newX, p.Y)
                #TODO přidat kontrolu, že se posunutý bod nepřekrývá
                shiftPoints.append(shiftPoint)
            # pokud bod nemá být posunut, přidej původní
            else:
                shiftPoints.append(p)

                # points.append(p)
                # points.append(symetricPoint)
            counter -= 1
        print("Count of shifted points: " + str(count))
        return shiftPoints

    @staticmethod
    def generateSymetricPoints(points, width):
        print("Generating symetric points...")
        # překlopím body v ose x
        symetricPts = []
        # points = []
        for p in points:
            sym = width / 2 - p.X
            symetricPoint = Point(width / 2 + sym, p.Y)
            symetricPts.append(symetricPoint)
            # points.append(p)
            # points.append(symetricPoint)
        return symetricPts



    def startSymetricPoints(width, height, n,  listOfPoints, symetricPoints, shiftX=False, shiftY=False, changeSize=0, pointSize=0, addPoints=False,removePoints=False, nrOfSets=0):

        f = plt.figure(figsize=(100*pixel/25.4, 100*pixel/25.4), dpi=100)  # muj monitor

        # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
        plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
        plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

        print("Plotting points...")
        for pt in listOfPoints:
            plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")
            # i = int(pt.X)
            # j = int(pt.Y)
            # plt.text(pt.X, pt.Y + 0.05, "({}, {})".format(i, j))


        print("-- Plotting symetric Points...")
        for pt in symetricPoints:

            plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")


        print("-- Plotting symetric Points DONE...")

        # plt.savefig(fname="A4_300_5.pdf", orientation='landscape',format='pdf', edgecolor="none")
        name = "img/100px/set" +str(nrOfSets) +" " + str(n) + "x10px_100px"+".png"
        plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
        plt.clf()  # clear figure after saving png

        if shiftX:
            # posunuti puvodnich bodu
            shifter = 0.1
            for i in range(4):
                # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
                plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
                plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

                ax = plt.gca()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axis('off')


                print("___ Shifting symetric points in X axe")
                shiftPts = DataGenerator.shiftX(listOfPoints, width=width, maxShift=0.2, shiftPercentage=shifter)
                print("___ Shifting symetric points in X axe Done")

                for pt in symetricPoints :
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")

                for pt in shiftPts:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")
                for pt in listOfPoints:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")

                name = "img/100px/set" +str(nrOfSets) + " shiftX=" + str(shifter)  + ".png"
                plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
                plt.clf()  # clear figure after saving png
                shifter += 0.1

        if removePoints:
            remover = 0.1

            for i in range(4):
                counter = len(listOfPoints)
                # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
                plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
                plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

                ax = plt.gca()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axis('off')

                for pt in symetricPoints :
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")

                rem_points = int(counter * remover)
                # delitel = counter / rem_points
                count = 0
                print("@ Removing points " + str(remover))
                for pt in listOfPoints:
                    if counter <= rem_points:
                        count += 1
                    else:
                        plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")
                    counter -= 1

                print("   Removed:" + str(count) + " points ")

                name = "img/100px/set" +str(nrOfSets) + " removed=" + str(remover) +".png"
                plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
                plt.clf()  # clear figure after saving png
                remover += 0.1

        if addPoints:
            adder = 0.1
            counter = len(listOfPoints)
            for i in range(4):
                add_points = int(counter * adder)
                addedPoints = DataGenerator.addRandomPoints(canvasWidth=width, canvasHeight=height, n=add_points, point_list=listOfPoints)

                # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
                plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
                plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

                ax = plt.gca()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axis('off')

                for pt in symetricPoints:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black",
                             markerfacecolor="black")

                for pt in addedPoints:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black",
                             markerfacecolor="black")


                name = "img/100px/set" + str(nrOfSets) + " added=" + str(adder) + ".png"
                plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
                plt.clf()  # clear figure after saving png
                adder += 0.1

    def doLentils(width, height, n,  listOfPoints, symetricPoints, shiftX=False, shiftY=False, changeSize=0,
                  pointSize=0, addPoints=False,removePoints=False, nrOfSets=0):

        f = plt.figure(figsize=(100*pixel/25.4, 100*pixel/25.4), dpi=100)  # muj monitor

        # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
        plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
        plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

        print("Plotting points...")
        for pt in listOfPoints:
            plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")
            # i = int(pt.X)
            # j = int(pt.Y)
            # plt.text(pt.X, pt.Y + 0.05, "({}, {})".format(i, j))


        print("-- Plotting symetric Points...")
        for pt in symetricPoints:

            plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")


        print("-- Plotting symetric Points DONE...")

        # plt.savefig(fname="A4_300_5.pdf", orientation='landscape',format='pdf', edgecolor="none")
        name = "img/100px/set" +str(nrOfSets) +" " + str(n) + "x10px_100px"+".png"
        plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
        plt.clf()  # clear figure after saving png

        if shiftX:
            # posunuti puvodnich bodu
            shifter = 0.1
            for i in range(4):
                # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
                plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
                plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

                ax = plt.gca()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axis('off')


                print("___ Shifting symetric points in X axe")
                shiftPts = DataGenerator.shiftX(listOfPoints, width=width, maxShift=0.2, shiftPercentage=shifter)
                print("___ Shifting symetric points in X axe Done")

                for pt in symetricPoints :
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")

                for pt in shiftPts:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")
                for pt in listOfPoints:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")

                name = "img/100px/set" +str(nrOfSets) + " shiftX=" + str(shifter)  + ".png"
                plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
                plt.clf()  # clear figure after saving png
                shifter += 0.1

        if removePoints:
            remover = 0.1

            for i in range(4):
                counter = len(listOfPoints)
                # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
                plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
                plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

                ax = plt.gca()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axis('off')

                for pt in symetricPoints :
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")

                rem_points = int(counter * remover)
                # delitel = counter / rem_points
                count = 0
                print("@ Removing points " + str(remover))
                for pt in listOfPoints:
                    if counter <= rem_points:
                        count += 1
                    else:
                        plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black", markerfacecolor="black")
                    counter -= 1

                print("   Removed:" + str(count) + " points ")

                name = "img/100px/set" +str(nrOfSets) + " removed=" + str(remover) +".png"
                plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
                plt.clf()  # clear figure after saving png
                remover += 0.1

        if addPoints:
            adder = 0.1
            counter = len(listOfPoints)
            for i in range(4):
                add_points = int(counter * adder)
                addedPoints = DataGenerator.addRandomPoints(canvasWidth=width, canvasHeight=height, n=add_points, point_list=listOfPoints)

                # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy - platno by se podle toho zmensilo
                plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
                plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

                ax = plt.gca()
                ax.get_xaxis().set_visible(False)
                ax.get_yaxis().set_visible(False)
                ax.axis('off')

                for pt in symetricPoints:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black",
                             markerfacecolor="black")

                for pt in addedPoints:
                    plt.plot(pt.X, pt.Y, marker="o", markersize=pointSize, markeredgecolor="black",
                             markerfacecolor="black")


                name = "img/100px/set" + str(nrOfSets) + " added=" + str(adder) + ".png"
                plt.savefig(fname=name, orientation='landscape', format='png', edgecolor="none")
                plt.clf()  # clear figure after saving png
                adder += 0.1


class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        # self.Z = 0

    def Equals(self, obj):
        other = obj if isinstance(obj, Point) else None

        return self.X == other.X and self.Y == other.Y
        # and self.Z == other.Z


if __name__ == "__main__":

    pixel = 0.27
    width = 100 * pixel   # 100px 1px= 0.27mm
    height = 100 * pixel    # 100px 1px= 0.27
    shiftedList = []

    nrOfPoints = 20
    nrOfChangedSizePoints = 0
    sizeOfPoints = 10 * pixel   # chci vel 10px a vim, ze pixel = 0.311 mm

    originalCanvasFactory = PointFactory.PointFactory(0, 0, width/2, height, nrOfPoints)
    originalCanvasFactory.generateRandomPointsWithNoOverlap()
    symmetricCanvasFactory = originalCanvasFactory.getSymmetricHalf(originalCanvasFactory)

    listOfPoints = []
    symetricPoints = []
    counter = 1

    for c in range(counter):

        plotterOriginal = PicFactory.PicFactory(width, height, pixel, "img/100px/original.png")
        plotterOriginal.drawPoints(originalCanvasFactory.getPoints() + symmetricCanvasFactory.getPoints())

        plotterShiftedX = PicFactory.PicFactory(width, height, pixel, "img/100px/shiftedX.png")
        plotterShiftedX.drawPoints(originalCanvasFactory.getShiftedPointsList(width * 0.4, 0.3) + symmetricCanvasFactory.getPoints())

        listOfPoints = DataGenerator.generateRandomPoints(canvasWidth=width, canvasHeight=height, n=nrOfPoints)
        symetricPoints = DataGenerator.generateSymetricPoints(listOfPoints, width=width)

        #DataGenerator.startSymetricPoints(width=width, height=height, n=nrOfPoints, listOfPoints=listOfPoints, symetricPoints=symetricPoints, shiftX=True, shiftY=False, changeSize=nrOfChangedSizePoints,pointSize=sizeOfPoints, addPoints=True, removePoints=True, nrOfSets=c)
        DataGenerator.startSymetricPoints(width=width, height=height, n=nrOfPoints, listOfPoints=originalCanvasFactory.getPoints(),
                                          symetricPoints=symmetricCanvasFactory.getPoints(), shiftX=True, shiftY=False,
                                          changeSize=nrOfChangedSizePoints, pointSize=sizeOfPoints, addPoints=True,
                                          removePoints=True, nrOfSets=c)
