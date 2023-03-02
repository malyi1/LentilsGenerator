from matplotlib import pyplot as plt


class PicFactory:
    """
        class contains info & settings & methods about plotting
    """

    def __init__(self, width, height, pixelSize, fileName):
        self.__width = width
        self.__height = height
        self.__pixelSize = pixelSize
        self.__fileName = fileName
        self.__figure = plt.figure(figsize=(2, 2))

        # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy -
        # platno by se podle toho zmensilo
        plt.plot(0, 0, marker="o", markersize=1, markeredgecolor="black", markerfacecolor="white")
        plt.plot(width, height, marker="o", markersize=1, markeredgecolor="black", markerfacecolor="white")

        # settings
        plt.tight_layout(pad=0.0)
        plt.margins(x=0.0, y=0.0)
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

    def drawPoints(self, pointsList):
        for point in pointsList:
            plt.plot(point.X, point.Y, marker="o", markersize=point.getDiameter(), markeredgecolor="black",
                     markerfacecolor="black", zorder=10)

        plt.tight_layout(pad=0.0)
        plt.savefig(fname=self.__fileName, orientation='landscape', format='png', edgecolor="none")
        plt.clf()  # clear figure after saving png

    def drawSymmetricPolygon(self, pointsList, symmetricPointsList):
        x = []
        y = []
        xs = []
        ys = []

        for point in pointsList:
            x.append(point.X)
            y.append(point.Y)

        for point in symmetricPointsList:
            xs.append(point.X)
            ys.append(point.Y)

        plt.plot(x, y)
        plt.plot(xs, ys)
        plt.tight_layout(pad=0.0)
        plt.savefig(fname=self.__fileName, orientation='landscape', format='png', edgecolor="none")
        plt.clf()
