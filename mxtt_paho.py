from PySide6.QtCore import QThread, Signal
from debug import debug
import paho.mqtt.client as paho

class MQTTClient(QThread):
    """
    Cliente MQTT ejecutado en un hilo independiente usando QThread.
    
    - Maneja la conexión a un broker MQTT (con soporte TLS).
    - Permite publicar y suscribirse a topics.
    - Emite señales hacia la UI cada vez que se recibe un mensaje.
    
    Señales
    -------
    data_received : Signal(str, str)
        Emitida al recibir un mensaje MQTT.
        Parámetros: (topic, payload)
    """
    data_received = Signal(str, str)

    def __init__(self, url, port, username, password, use_tls=False):
        super().__init__()
        self.broker = url
        self.port = port
        self.username = username
        self.password = password
        self.use_tls = use_tls
        
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION2)
        self.client.username_pw_set(self.username, self.password)
        if self.use_tls:
            self.client.tls_set()
        
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        
    def on_connect(self, client, userdata, flags, reason_code, properties=None):
        """
        Callback ejecutado al establecer conexión con el broker.
        reason_code == 0 → conexión exitosa
        """
        debug(f"[MQTT] CONNACK received with code \'{reason_code}\'")
                
    def on_disconnect(self, client, userdata, disconnect_flags, reason_code,  properties=None):
        """
        Callback ejecutado al desconectarse del broker.
        reason_code == 0 → desconexión solicitada
        reason_code != 0 → desconexión inesperada
        """
        debug(f"[MQTT] Disconnected with result code \'{reason_code}\'")
        if reason_code != 0:
            debug("[MQTT] Unexpected disconnection, retrying...")

    def publish(self, topic, payload):
        """
        Publica un mensaje en el broker.
        """
        self.client.publish(topic, payload)
        debug(f"[MQTT] Published \'{topic} : {payload}\'")

    def subscribe(self, topic):
        """
        Se suscribe a un topic para recibir mensajes.
        """
        self.client.subscribe(topic)
        
    def on_message(self, client, userdata, msg):
        """
        Callback ejecutado al recibir un mensaje de un topic suscrito.
        """
        topic = msg.topic
        payload = msg.payload.decode()
        debug(f"[MQTT] Message received \'{topic} : {payload}\'")
        self.data_received.emit(topic, payload)

    def run(self):
        """
        Hilo del cliente MQTT.
        - Conecta al broker.
        - Entra en loop_forever() para mantener la conexión activa.
        - Hilo bloqueante.
        """
        debug("[MQTT] Thread starting")
        try:
            self.client.connect(self.broker, self.port, keepalive=30)
            self.client.loop_forever(retry_first_connection=True)
        except Exception as e:
            debug(f"[MQTT] Connection error \'{e}\'")
    
    def stop(self):
        """
        Detiene el hilo y desconecta del broker.
        """
        debug("[MQTT] Stopping thread and disconnecting...")
        try:
            self.client.disconnect()
        except Exception as e:
            debug(f"[MQTT] Error on disconnect: {e}")
        self.quit()
        self.wait()