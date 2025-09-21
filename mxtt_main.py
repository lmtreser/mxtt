import sys
from PySide6.QtWidgets import QApplication, QWidget
from .ui/mxtt_ui import Ui_Form
from mxtt_driver import MXTTDriver

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mqtt_driver = MXTTDriver(self)
        
    def closeEvent(self, event):
        """Se ejecuta automáticamente al cerrar la ventana."""
        self.mqtt_driver.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())