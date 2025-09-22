import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from ui.mxtt_ui import Ui_Form
from mxtt_driver import MXTTDriver
import ui.resources_rc

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mqtt_driver = MXTTDriver(self)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))
        
    def closeEvent(self, event):
        """Se ejecuta automáticamente al cerrar la ventana."""
        self.mqtt_driver.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())