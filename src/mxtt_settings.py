from PySide6.QtCore import QSettings
from debug import debug

class MXTTSettings: 
    """
    Clase para gestionar la configuración del broker MQTT usando QSettings.

    Permite guardar y cargar la configuración de conexión (URL, puerto, TLS, usuario, contraseña).
    """
    
    def __init__(self):
        """
        Inicializa QSettings con la organización 'LMT' y la aplicación 'MXTT'.
        """
        self.settings = QSettings("LMT", "MXTT")

    def save_broker(self, url, port=1883, tls=False, username="", password=""):     
        """
        Guarda la configuración actual del broker en QSettings.

        Args:
            url (str): Dirección del broker MQTT.
            port (int, optional): Puerto TCP. Por defecto 1883.
            tls (bool, optional): True para habilitar TLS. Por defecto False.
            username (str, optional): Nombre de usuario para autenticación. Por defecto cadena vacía.
            password (str, optional): Contraseña para autenticación. Por defecto cadena vacía.

        Returns:
            None
        """
        self.settings.setValue("broker/url", url)
        self.settings.setValue("broker/port", port)
        self.settings.setValue("broker/tls", tls)
        self.settings.setValue("broker/username", username)
        self.settings.setValue("broker/password", password)
        debug("[SETTINGS] Config saved successfully.")

    def load_broker(self):
        """
        Carga la configuración del broker desde QSettings.

        Returns:
            dict: Diccionario con la configuración, con claves:
                - 'url' (str)
                - 'port' (int)
                - 'tls' (bool)
                - 'username' (str)
                - 'password' (str)
        """
        return {
            "url" : self.settings.value("broker/url"),
            "port" : self.settings.value("broker/port"),
            "tls" : self.settings.value("broker/tls"),
            "username" : self.settings.value("broker/username"),
            "password" : self.settings.value("broker/password")
        }