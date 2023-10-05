from PyQt6.QtCore import QThread, pyqtSignal

class Worker(QThread):
    # Define a signal to emit the result
    finished_signal = pyqtSignal(object)  # Use a generic object to allow different result types

    def __init__(self, function_to_run):
        super().__init__()
        self.function_to_run = function_to_run

    def run(self):
        result = self.function_to_run()
        self.finished_signal.emit(result)
