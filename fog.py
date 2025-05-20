import paho.mqtt.client as mqtt
import json
from datetime import datetime
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin

# Inicializa o Firebase apenas uma vez
if not firebase_admin._apps:
    cred = credentials.Certificate("aula-pos-iot-firebase-adminsdk-fbsvc-83d07bc95e.json")
    initialize_app(cred)

db = firestore.client()

# Configurações MQTT
BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "aviario/teste"

# Função de conexão
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("🟢 Conectado ao HiveMQ!")
        client.subscribe(TOPIC)
        print(f"📡 Assinado ao tópico: {TOPIC}")
    else:
        print("🔴 Falha na conexão. Código:", rc)

# Função de recebimento de mensagem
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"[{timestamp}] Dados recebidos: {payload}")

        # Dados para enviar ao Firebase
        dados_firebase = {
            "temperatura": payload["temperatura"],
            "umidade": payload["umidade"],
            "status": payload["status"],
            "timestamp": timestamp
        }

        db.collection("leituras_aviario").add(dados_firebase)
        print("📤 Enviado para o Firebase!")

    except Exception as e:
        print("Erro ao processar mensagem:", e)

# Inicia cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("🔄 Conectando ao broker MQTT...")
client.connect(BROKER, PORT, 60)
client.loop_forever()
