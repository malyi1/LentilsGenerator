# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from scipy.ndimage import gaussian_filter
from matplotlib.image import imread


class PicFactory:
    """
        class contains info & settings & methods about plotting
    """

    def __init__(self, width, height, fileName, backgroundColor = "Black", foregroundColor="White", pointColor="Yellow", canvasWidth=None, canvasHeight=None):
        self.__width = width
        self.__height = height
        self.__fileName = fileName
        
        self.__canvasWidth = canvasWidth if canvasWidth is not None else width
        self.__canvasHeight = canvasHeight if canvasHeight is not None else height

        self.__backgroundColor = backgroundColor
        self.__foregroundColor = foregroundColor
        self.__pointColor = pointColor

        # self.__figure = plt.figure(figsize=(2, 2), dpi=100)
        self.__figure = plt.figure(figsize=(self.__canvasWidth / 100, self.__canvasHeight / 100), dpi=100)

        # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy -
        # platno by se podle toho zmensilo
        plt.plot(0, 0, marker="o", markersize=1, markeredgecolor="white", markerfacecolor="white")
        plt.plot(self.__canvasWidth, self.__canvasHeight, marker="o", markersize=1, markeredgecolor="white", markerfacecolor="white")
        # nahrazeno kreslenim pozadi

        # settings  - we want canvas without axes and grid
        plt.tight_layout(pad=0.0)
        plt.margins(x=0.0, y=0.0)

        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

        # draw empty canvas
        ax.add_patch(Rectangle((0, 0), self.__canvasWidth, self.__canvasHeight, color=self.__backgroundColor, zorder=-2))
        ax.add_patch(Circle((self.__canvasWidth / 2, self.__canvasHeight / 2), self.__width / 2, color=self.__foregroundColor, zorder=-1))


    # draw the points from given pointlist on the grid
    def drawPoints(self, pointsList):
        leftX = self.__canvasWidth / 2 - self.__width / 2
        leftY = self.__canvasHeight / 2 - self.__height / 2

        for point in pointsList:
            # plt.plot(leftX + point.X, leftY + point.Y, marker="o", markersize=point.getDiameter(), 
            #         markerfacecolor=self.__pointColor, zorder=10, markeredgewidth=0)
            plt.plot(leftX + point.X, leftY + point.Y, marker="o", markersize=point.getDiameter() -5 , 
                    markerfacecolor=self.__pointColor, zorder=10, markeredgewidth=0)

            alphas = [0.7, 0.5, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1, 0.05, 0.025]
            for i, alpha in enumerate(alphas):
                # plt.plot(leftX + point.X, leftY + point.Y, marker="o", markersize=point.getDiameter() / (i+1), 
                #      markerfacecolor=self.__pointColor, zorder=10, markeredgewidth=0, alpha=alpha)
                plt.plot(leftX + point.X, leftY + point.Y, marker="o", markersize=point.getDiameter() -5 + i, 
                     markerfacecolor=self.__pointColor, zorder=10, markeredgewidth=0, alpha=alpha)

        plt.tight_layout(pad=0.0)
        plt.savefig(fname=self.__fileName, orientation='landscape', format='png', edgecolor="none")

        # img = imread(self.__fileName)
        # # Apply Gaussian filter
        # # sigma is the standard deviation of the Gaussian filter. You can adjust it as needed.
        # sigma = 1
        # filtered_img = gaussian_filter(img, sigma=sigma)
        # # Display filtered image
        # plt.subplot(1, 2, 2)
        # plt.imshow(filtered_img)

        # plt.savefig(fname="g"+self.__fileName, orientation='landscape', format='png', edgecolor="none")

        plt.clf()  # clear figure after saving png
        plt.close() # close figure after saving png

    # def finalizeAndSave(self):
    #     plt.savefig(fname=self.__fileName, orientation='landscape', format='png', edgecolor="none")
    #     plt.clf()  # clear figure after saving png
    #     plt.close() # close figure after saving png
