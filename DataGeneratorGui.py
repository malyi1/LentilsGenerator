from PyQt6 import QtWidgets
from ui.MainWindow_UI import Ui_MainWindow
from generator.DataGenerator import DataGenerator
from ui_utils.Worker import Worker

class DataGeneratorGui():

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.changeBackgroundColorButton.setStyleSheet("background-color:{};".format(self.ui.canvasBackgroundText.text()))
        self.ui.changeCircleColorButton.setStyleSheet("background-color:{};".format(self.ui.circleColorText.text()))
        self.ui.changePointColorButton.setStyleSheet("background-color:{};".format(self.ui.pointColorText.text()))

        self.ui.generatePushButton.clicked.connect(lambda: self.start_foreground_work(self.run_generate, self.beforeRunGenerate, self.afterRunGenerate))
        self.ui.changeBackgroundColorButton.clicked.connect(lambda: self.setColor(self.ui.canvasBackgroundText, self.ui.changeBackgroundColorButton))
        self.ui.changeCircleColorButton.clicked.connect(lambda: self.setColor(self.ui.circleColorText, self.ui.changeCircleColorButton))
        self.ui.changePointColorButton.clicked.connect(lambda: self.setColor(self.ui.pointColorText, self.ui.changePointColorButton))
        self.MainWindow.show()

    def run_generate(self):
        DataGenerator.generateLentils(
            self.ui.widthSpinBox.value(),
            self.ui.heightSpinBox.value(),
            int(self.ui.noOfPointsSpinBox.value() / 2),
            self.ui.sizeOfPointsSpinBox.value(),
            self.ui.setCountSpinBox.value(),
            self.ui.sigmaDoubleSpinBox.value(),
            self.ui.canvasWidthSpinBox.value(),
            self.ui.canvasHeightSpinBox.value(),
            self.ui.maxShiftSpinBox.value(),
            self.ui.canvasBackgroundText.text(),
            self.ui.circleColorText.text(),
            self.ui.pointColorText.text(),
        )

    def beforeRunGenerate(self):
        self.ui.generatePushButton.setEnabled(False)

    def afterRunGenerate(self):
        self.ui.generatePushButton.setEnabled(True)

    def start_foreground_work(self, lambdaOnBackground, beforeUpdateUi, afterUpdateUi):
        beforeUpdateUi()
        lambdaOnBackground()
        afterUpdateUi()
    
    def start_background_work(self, lambdaOnBackground, beforeUpdateUi, afterUpdateUi):
        self.worker = Worker(lambdaOnBackground)

        beforeUpdateUi()
        self.worker.finished_signal.connect(afterUpdateUi)
        self.worker.start()

    @staticmethod
    def setColor(textEdit, button):
        dialog = QtWidgets.QColorDialog()
        dialog.setOption(QtWidgets.QColorDialog.ColorDialogOption.ShowAlphaChannel, on=True)
        newColor = QtWidgets.QColorDialog.getColor().name()
        textEdit.setText(newColor)
        button.setStyleSheet("background-color:{};".format(newColor))
        dialog.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    dataGeneratorGui = DataGeneratorGui()
    
    sys.exit(app.exec())

