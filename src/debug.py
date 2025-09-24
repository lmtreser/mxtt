# debug.py
from icecream import ic
from datetime import datetime

_debug_callback = None
DEBUG_ENABLED = True

def timestamp_prefix():
    return f"[{datetime.now().strftime('%H:%M:%S')}] "
ic.configureOutput(prefix=timestamp_prefix)

def set_debug_callback(callback):
    """
    Registra una función de callback para redirigir los mensajes de debug.
    """
    global _debug_callback
    _debug_callback = callback

def debug(*args, **kwargs):
    """Función de debug centralizada, compatible con UI y consola."""
    if DEBUG_ENABLED:
        msg = " ".join(str(a) for a in args)
        ic(msg, **kwargs)
        if _debug_callback:
            _debug_callback(msg)

debug("[DEBUG] Debugging enabled")