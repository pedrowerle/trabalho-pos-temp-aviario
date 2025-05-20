# 🐔 Aviário IoT - Monitoramento de Temperatura com ESP32, MQTT, Firebase e Streamlit

Solução completa de IoT para controle térmico em aviários, monitorando temperatura e umidade em tempo real com painel web interativo.

## 🎯 Objetivo

Fornecer ferramenta inteligente para monitoramento ambiental em aviários:
- Redução de mortalidade por estresse térmico
- Aumento da produtividade das aves
- Tomada de decisão ágil com dados em tempo real

## 🔧 Tecnologias Utilizadas

- **Hardware**:
  - ESP32 (simulado via [Wokwi](https://wokwi.com/))
  - Sensor DHT22 (temperatura/umidade)

- **Software**:
  - MQTT (broker [HiveMQ](https://www.hivemq.com/))
  - Firebase Firestore (banco de dados)
  - Streamlit (dashboard)
  - Python com:
    - `paho-mqtt`
    - `firebase-admin`

## 🧠 Funcionalidades Principais

### Coleta de Dados (ESP32)
- Leitura contínua de temperatura/umidade
- Transmissão via Wi-Fi para broker MQTT
- Alerta visual (LED) para temperaturas fora da faixa ideal (21°C-26°C)

### Processamento (Python)
- Recebimento dos dados via MQTT
- Armazenamento no Firebase com timestamp
- Ponte entre dispositivo e nuvem

### Visualização (Streamlit)
- Dashboard web atualizado automaticamente
- Gráficos temporais interativos
- Histórico das últimas leituras
- Classificação do status térmico

## 📂 Estrutura do Projeto

```
aviario-iot/
├── fog.py                      # Recebe dados via MQTT e envia ao Firebase
├── dashboard.py                # Interface com Streamlit
├── firebase_config.py          # Inicialização do Firebase
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

---

