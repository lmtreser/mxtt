# MXTT MQTT Explorer

Aplicación de escritorio para **monitoreo y control de sistemas IoT mediante MQTT**, desarrollada en Python con **PySide6 / Qt6**.

MXTT es una herramienta educativa y de prototipado rápido que permite:

- Conectar dispositivos IoT vía MQTT.
- Visualizar datos en tiempo real.
- Controlar actuadores mediante una interfaz gráfica moderna.

La UI se creó con **Qt Designer** y se encuentra en la carpeta `ui`. Los recursos (iconos, imágenes) se pueden integrar con **Qt Resource System** (`.qrc`) dentro de la misma carpeta.

## Requisitos

- Python 3.9 o superior
- PySide6
- [paho.mqtt.python](https://github.com/eclipse-paho/paho.mqtt.python)
- [icecream](https://github.com/gruns/icecream)
- Qt Designer (opcional)

## Estructura del proyecto

```
mxtt-app/
├─ mxtt_main.py             # Script principal
├─ ui/
│   ├─ resources/
│   │     ├─ mxtt_ui.ui     # UI creada en Qt Designer
│   │     ├─ icons_rc.qrc   # Archivo de recursos
│   │     ├─ mqtt.ico       # Icono (ico)
│   │     └─ mqtt.svg       # Icono (svg)
│   ├─ __init__.py
│   ├─ mxtt_ui.py           # UI compilada a Python
│   └─ resources.py         # Recursos (compilado)
├─ mqtt_driver.py           # Lógica ui/mqtt/file
├─ mxtt_paho.py             # Conexión MQTT
├─ mxtt_logger.py           # Depuración a archivo
├─ mxtt_settings.py         # Almacenar y recuperar configuración
├─ debug.py                 # Depuración mediante IceCream
├─ README.md                # Documentación
└─ LICENSE                  # Licencia MIT
```

## Uso



## Licencia

* Proyecto desarrollado bajo **licencia MIT**.
* Compatible con **PySide6 (LGPL)**, libre para proyectos comerciales o educativos.

## Contribuciones

* Pull requests y sugerencias son bienvenidas.
* Antes de contribuir, asegurarse de mantener compatibilidad con **Python 3.9+** y conservar la estructura de la UI en la carpeta `ui`.
