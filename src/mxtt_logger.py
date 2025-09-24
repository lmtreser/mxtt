# mxtt_logger.py
from pathlib import Path
from datetime import datetime
from debug import debug

class MXTTLogger:
    """
    Logger de debug opcional a archivo.

    Permite habilitar o deshabilitar el guardado de mensajes de debug
    en un archivo de texto con timestamp.
    """
    def __init__(self, filename: str = "mxtt.log"):
        """
        Inicializa el logger con el archivo de destino.

        Args:
            filename (str, optional): Nombre o ruta del archivo de log.
                Por defecto ``"mxtt.log"``.
        """
        self.filepath = Path(filename)
        self.enabled = False

    def set_enabled(self, enabled: bool):
        """
        Habilita o deshabilita el logging a archivo.

        Args:
            enabled (bool): ``True`` para habilitar, ``False`` para deshabilitar.

        Returns:
            None
        """
        self.enabled = enabled
        debug(f"[LOGGER] Logging to file {'enabled' if enabled else 'disabled'}")

    def log(self, msg: str):
        """
        Si está habilitado, escribe el mensaje en el archivo con timestamp.

        Args:
            msg (str): Mensaje a registrar.

        Returns:
            None
        """
        if self.enabled:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            try:
                with self.filepath.open("a", encoding="utf-8") as f:
                    f.write(f"{timestamp} {msg}\n")
            except Exception as e:
                debug(f"[LOGGER] Error writing to log file: {e}")
