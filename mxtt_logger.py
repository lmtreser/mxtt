# mxtt_logger.py
from pathlib import Path
from datetime import datetime
from debug import debug

class MXTTLogger:
    """
    Logger de debug opcional a archivo.
    """
    def __init__(self, filename: str = "mxtt.log"):
        self.filepath = Path(filename)
        self.enabled = False

    def set_enabled(self, enabled: bool):
        """Habilita o deshabilita el logging a archivo."""
        self.enabled = enabled
        debug(f"[LOGGER] Logging to file {'enabled' if enabled else 'disabled'}")

    def log(self, msg: str):
        """Si está habilitado, escribe el mensaje en el archivo con timestamp."""
        if self.enabled:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            try:
                with self.filepath.open("a", encoding="utf-8") as f:
                    f.write(f"{timestamp} {msg}\n")
            except Exception as e:
                debug(f"[LOGGER] Error writing to log file: {e}")
