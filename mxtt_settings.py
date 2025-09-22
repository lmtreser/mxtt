from PySide6.QtCore import QSettings
from debug import debug

class MXTTSettings: 
    
    def __init__(self):
        self.settings = QSettings("LMT", "MXTT")

    def save_broker(self, url, port=1883, tls=False, username="", password=""):     
        """
        Guarda la configuración actual de la UI en QSettings.
        """
        self.settings.setValue("broker/url", url)
        self.settings.setValue("broker/port", port)
        self.settings.setValue("broker/tls", tls)
        self.settings.setValue("broker/username", username)
        self.settings.setValue("broker/password", password)
        debug("[SETTINGS] Config saved successfully.")

    def load_broker(self):
        """
        Carga la configuración desde QSettings y la vuelca a la UI.
        """
        return {
            "url" : self.settings.value("broker/url"),
            "port" : self.settings.value("broker/port"),
            "tls" : self.settings.value("broker/tls"),
            "username" : self.settings.value("broker/username"),
            "password" : self.settings.value("broker/password")
        }