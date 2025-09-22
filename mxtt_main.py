import sys, ui.resources_rc
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from ui.mxtt_ui import Ui_Form
from mxtt_driver import MXTTDriver
from debug import set_debug_callback
from mxtt_settings import MXTTSettings
from mxtt_logger import MXTTLogger

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/mqtt.svg"))
        
        self.app_settings = MXTTSettings()
        self.mqtt_driver = MXTTDriver(self, self.app_settings)
        
        self.logger = MXTTLogger("mxtt.log")
        self.ui.check_log_to_file.stateChanged.connect(self.toggle_file_logging)
        set_debug_callback(self.append_debug)

    def toggle_file_logging(self, state):
        """Habilita o deshabilita el logging a archivo."""
        self.logger.set_enabled(state)
        
    def append_debug(self, text):
        """Agrega una línea al tab Debug."""
        self.ui.pte_debug.appendPlainText(text)
        self.logger.log(text)
        
    def closeEvent(self, event):
        """Se ejecuta automáticamente al cerrar la ventana."""
        self.mqtt_driver.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())