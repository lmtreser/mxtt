from mxtt_paho import MQTTClient
from debug import debug

class MXTTDriver:
    """
    Controlador que conecta mxtt_ui con mxtt_paho.
    Maneja los eventos de los botones y actualiza la interfaz.    
    """

    def __init__(self, view, settings):
        self.view = view
        self.settings = settings
        self.mqtt_client = None
    
        # Input fields, topic config
        self.view.ui.pb_subscribe.clicked.connect(self.subscribe_to_topic)        
        # Push buttons
        self.view.ui.pb_connect.clicked.connect(self.connect_to_broker)
        self.view.ui.pb_config_save.clicked.connect(self.save_config)
        # Tab Messages
        self.view.ui.pb_send.clicked.connect(self.send_message)
        # Cargar configuración guardada
        self.load_config()

    def subscribe_to_topic(self):
        """
        Suscribe al cliente MQTT a un topic ingresado en el input correspondiente.
        """
        topic = self.view.ui.input_topic_1.text()
        if self.mqtt_client:
            self.mqtt_client.subscribe(topic)
            debug(f"[DRIVER] Subscribed to topic \'{topic}\'")
        else:
            debug("[DRIVER] Cannot subscribe, MQTT client not connected.")
    
    def send_message(self):
        """
        Envía un mensaje al broker MQTT.
        El input debe tener el formato: 'topic : payload'
        """
        # ToDo: Validar input
        message = self.view.ui.input_send_msg.text()
        topic = message.split(" : ")[0]
        payload = message.split(" : ")[1]
        if self.mqtt_client:
            self.mqtt_client.publish(topic, payload)
            debug(f"[DRIVER] Sent message \'{topic} : {payload}\'")
        else:
            debug("[DRIVER] Cannot send message, MQTT client not connected.")
    
    def update_message(self, topic, payload):
        """
        Callback que se ejecuta al recibir un mensaje MQTT.
        Actualiza la lista de mensajes en la UI.
        """
        self.view.ui.listView_msg.addItem(f"{topic} : {payload}")
        debug(f"[DRIVER] Received message \'{topic} : {payload}\'")
    
    def save_config(self):
        """
        Guarda la configuración del cliente en un archivo.
        """
        debug("[DRIVER] Saving config...")
        self.settings.save_broker(
            url=self.view.ui.input_url.text(),
            port=int(self.view.ui.input_port.text()),
            tls=self.view.ui.check_tls.isChecked(),
            username=self.view.ui.input_user.text(),
            password=self.view.ui.input_password.text()
        )
    
    def load_config(self):
        """
        Carga la configuración del cliente desde un archivo.
        """
        debug("[SETTINGS] Loading config...")
        cfg_stored = self.settings.load_broker()
        self.view.ui.input_url.setText(cfg_stored["url"])
        self.view.ui.input_port.setText(str(cfg_stored["port"]))
        self.view.ui.check_tls.setChecked(cfg_stored["tls"] in [True, 'true', '1'])
        self.view.ui.input_user.setText(cfg_stored["username"])
        self.view.ui.input_password.setText(cfg_stored["password"])
        
    def connect_to_broker(self):
        """
        Conecta al broker MQTT creando un hilo independiente (QThread).
        Se configuran credenciales, puerto y TLS según la UI.
        """
        debug("[DRIVER] Connecting to broker MQTT")
        # ToDo: Validar inputs
        self.mqtt_client = MQTTClient(
            url=self.view.ui.input_url.text(),
            port=int(self.view.ui.input_port.text()),
            username=self.view.ui.input_user.text(),
            password=self.view.ui.input_password.text(),
            use_tls=self.view.ui.check_tls.isChecked()
        )
        debug(f"[DRIVER] Client created: {self.mqtt_client}")
        debug("[DRIVER] Attempting start thread...")
        self.mqtt_client.data_received.connect(self.update_message)
        self.mqtt_client.start()
        
    def close(self):
        """Cierra la conexión MQTT y detiene el hilo al cerrar la aplicación."""
        debug("[DRIVER] Closing MXTTDriver.")
        if self.mqtt_client:
            self.mqtt_client.stop()
            self.mqtt_client = None
