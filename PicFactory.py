from matplotlib import pyplot as plt

class PicFactory:

    def __init__(self, width, height, pixelSize, fileName):
        self.__width = width
        self.__height = height
        self.__pixelSize = pixelSize
        self.__fileName = fileName
        self.__figure = plt.figure(figsize=(100*pixelSize/25.4, 100*pixelSize/25.4), dpi=100)  #muj monitor

        # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy -
        # platno by se podle toho zmensilo
        plt.plot(0, 0, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")
        plt.plot(width, height, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="white")

        # settings
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

    def drawPoints(self, pointsList):

        for point in pointsList:
            plt.plot(point.X, point.Y, marker="o", markersize=point.getDiameter(), markeredgecolor="black", markerfacecolor="black")

        plt.savefig(fname=self.__fileName, orientation='landscape', format='png', edgecolor="none")
        plt.clf()  # clear figure after saving png