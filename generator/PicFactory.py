# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from scipy.ndimage import gaussian_filter
from matplotlib.image import imread
from io import BytesIO
import cv2
import numpy as np
from PIL import Image, ImageDraw

class PicFactory:
    """
        class contains info & settings & methods about plotting
    """

    def __init__(self, width, height, fileName, pointDiameter, sigma, backgroundColor = "Black", foregroundColor="White", pointColor="Yellow", canvasWidth=None, canvasHeight=None):
        self.__width = width
        self.__height = height
        self.__fileName = fileName
        
        self.__canvasWidth = canvasWidth if canvasWidth is not None else width
        self.__canvasHeight = canvasHeight if canvasHeight is not None else height

        self.__backgroundColor = backgroundColor
        # self.__foregroundColor = (0.5, 0.5, 0.5)
        # self.__pointColor = (0, 0.4, 0)
        self.__foregroundColor = foregroundColor
        self.__pointColor = pointColor

        self.__pointDiameter = pointDiameter

        self.__sigma = sigma

        # self.__figure = plt.figure(figsize=(2, 2), dpi=100)
        self.__figure = plt.figure(figsize=(self.__canvasWidth / 100, self.__canvasHeight / 100), dpi=100)

        # pouze pomucka pro ziskani vzdy celeho platna pro pripad ze by data byly vygenerovany jen u osy -
        # platno by se podle toho zmensilo
        plt.plot(0, 0, marker="o", markersize=1, markeredgecolor=self.__pointColor, markerfacecolor=self.__pointColor)
        plt.plot(self.__canvasWidth, self.__canvasHeight, marker="o", markersize=1, markeredgecolor=self.__pointColor, markerfacecolor=self.__pointColor)
        # nahrazeno kreslenim pozadi

        # settings  - we want canvas without axes and grid
        plt.tight_layout(pad=0.0)
        plt.margins(x=0.0, y=0.0)

        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.axis('off')

        # draw empty canvas
        ax.add_patch(Rectangle((0, 0), self.__canvasWidth, self.__canvasHeight, color=self.__foregroundColor, zorder=-2))
        # ax.add_patch(Circle((self.__canvasWidth / 2, self.__canvasHeight / 2), self.__width / 2, color=self.__foregroundColor, zorder=-1))
        # ax.add_patch(Rectangle((0, 0), self.__canvasWidth, self.__canvasHeight, color=self.__foregroundColor, zorder=-2))

        self.__img = Image.new('RGBA', (4*self.__canvasWidth, 4*self.__canvasHeight), backgroundColor)
        draw = ImageDraw.Draw(self.__img)
        draw.ellipse(((4 * self.__canvasWidth / 2) - (4 * self.__width / 2), (4 * self.__canvasHeight / 2) - (4 * self.__height / 2), (4 * self.__canvasWidth / 2) + (4 * self.__width / 2), (4 * self.__canvasHeight / 2) + (4 * self.__height / 2)), fill=(0, 0, 0, 0))
        self.__img.save('test.png', 'PNG', dpi=(100, 100))
        self.__img2 = self.__img.resize((self.__canvasWidth, self.__canvasHeight), resample=Image.LANCZOS)
        self.__img2.save('test1.png', 'PNG', dpi=(100, 100))


    # draw the points from given pointlist on the grid
    def drawPoints(self, pointsList):
        leftX = self.__canvasWidth / 2 - self.__width / 2
        leftY = self.__canvasHeight / 2 - self.__height / 2

        for point in pointsList:
            plt.plot(leftX + point.X, leftY + point.Y, marker="o", markersize=point.getDiameter(), 
                    markerfacecolor=self.__pointColor, zorder=10, markeredgewidth=0)

        plt.tight_layout(pad=0.0)

        buf = BytesIO()
        plt.savefig(buf, orientation='landscape', format='png', edgecolor="none", dpi=100)
        buf.seek(0)

        plt.clf()  # clear figure after saving png
        plt.close() # close figure after saving png

        image = cv2.imdecode(np.frombuffer(buf.read(), np.uint8), 1)
        # Gaussian Blur 
        Gaussian = cv2.GaussianBlur(image, [0,0], sigmaX = self.__sigma, sigmaY = self.__sigma) # 1.6
        # cv2.imwrite("g"+self.__fileName, Gaussian)
        buf2 = BytesIO()
        # cv2.imwrite(buf2, Gaussian)
        is_success, buffer = cv2.imencode(".png", Gaussian)
        buf2 = BytesIO(buffer)
        buf2.seek(0)

        #backgroundImg = Image.open("g"+self.__fileName)
        backgroundImg = Image.open(buf2)
        backgroundImgA = backgroundImg.convert("RGBA")
        # foregroundImg = Image.open("mask2.png")
        # foregroundImgA = foregroundImg.convert("RGBA")

        Image.alpha_composite(backgroundImgA, self.__img2).save(self.__fileName, dpi=(100, 100))

