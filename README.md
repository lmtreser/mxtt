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

La aplicación está dividida en varias pestañas (tabs). A saber:

### Broker

En esta pestaña se configuran los parámetros de conexión al broker MQTT.

- URL: Dirección del broker.
- Port: Puerto del servicio MQTT.
- TLS: Activar esta casilla si el broker requiere conexión segura.
- User: Usuario de autenticación (si el broker lo solicita).
- Password: Clave asociada al usuario.
- Topic: Tópico principal para suscribirse de manera rápida.
- Subscribe: Botón para suscribirse al tópico ingresado.
- Save Config: Guarda los parámetros de conexión.
- Connect: Establece la conexión con el broker.

**Ejemplo de uso**

1. Ingresar `test.mosquitto.org` en **URL**.
2. Poner puerto `1883`.
3. Dejar sin tildar la casilla **TLS**.
4. Presionar **Connect**.
5. Estado de conexión listo para enviar/recibir mensajes.

### Messages

Aquí se administran los mensajes MQTT.

- Lista de mensajes: Muestra los mensajes recibidos con sus tópicos.
- Caja de envío: Escribir un mensaje con el formato `topic : valor`.
- Send: Envía el mensaje al broker en el tópico indicado.

**Ejemplo de uso**

1. Suscribirse en la pestaña **Broker** al tópico `casa/luz`.
2. En la pestaña **Messages**, enviar `casa/luz : OFF`.
3. El mensaje aparece en la lista junto con cualquier respuesta de otros clientes conectados.

### **Debug**

Sirve para depurar y revisar lo que ocurre en la comunicación.

- Área de texto: Muestra logs en tiempo real (conexiones, errores, mensajes enviados/recibidos en bruto).
- Log to File: Activa el guardado de los logs en un archivo externo.

### **About**

Muestra información general sobre la aplicación:

## ToDo

- [ ] Validar inputs
- [ ] Agregar botón de desconexión
- [ ] Permitir guardar varios brokers
- [ ] Hashear password
- [-] Documentar

## Contribuciones

* Pull requests y sugerencias son bienvenidas.
* Antes de contribuir, asegurarse de mantener compatibilidad con **Python 3.9+** y conservar la estructura de la UI en la carpeta `ui`.

## Licencia

* Proyecto desarrollado bajo **licencia MIT**.
* Compatible con **PySide6 (LGPL)**, libre para proyectos comerciales o educativos.
