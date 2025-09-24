# debug.py
from icecream import ic
from datetime import datetime

_debug_callback = None
DEBUG_ENABLED = True

def timestamp_prefix():
    """
    Genera un prefijo de timestamp para los mensajes de debug.

    Returns:
        str: Hora actual en formato ``[HH:MM:SS] ``.
    """
    return f"[{datetime.now().strftime('%H:%M:%S')}] "

ic.configureOutput(prefix=timestamp_prefix)

def set_debug_callback(callback):
    """
    Registra una función de callback para redirigir los mensajes de debug.
    Args:
        callback (Callable[[str], None]): Función que recibe el mensaje de debug.
    """
    global _debug_callback
    _debug_callback = callback

def debug(*args, **kwargs):
    """
    Función de debug centralizada, compatible con UI y consola.

    Args:
        *args: Mensajes o valores a mostrar.
        **kwargs: Argumentos adicionales para ``icecream.ic``.

    Returns:
        None
    """
    if DEBUG_ENABLED:
        msg = " ".join(str(a) for a in args)
        ic(msg, **kwargs)
        if _debug_callback:
            _debug_callback(msg)

debug("[DEBUG] Debugging enabled")