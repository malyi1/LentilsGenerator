from PyQt6 import QtWidgets
from ui.MainWindow_UI import Ui_MainWindow
from generator.DataGenerator import DataGenerator
from ui_utils.Worker import Worker

class DataGeneratorGui():

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.generatePushButton.clicked.connect(lambda: self.start_foreground_work(self.run_generate, self.beforeRunGenerate, self.afterRunGenerate))
        self.MainWindow.show()

    def run_generate(self):
        DataGenerator.generateLentils(
            self.ui.widthSpinBox.value(),
            self.ui.heightSpinBox.value(),
            int(self.ui.noOfPointsSpinBox.value() / 2),
            self.ui.sizeOfPointsSpinBox.value(),
            self.ui.setCountSpinBox.value(),
            self.ui.canvasWidthSpinBox.value(),
            self.ui.canvasHeightSpinBox.value(),
            self.ui.canvasBackgroundText.text(),
            self.ui.circleColorText.text(),
            self.ui.pointColorText.text()
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    dataGeneratorGui = DataGeneratorGui()
    
    sys.exit(app.exec())

