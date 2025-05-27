# 🐔 Aviário IoT - Monitoramento de Temperatura com ESP32, MQTT, Firebase e Streamlit

Solução completa de IoT para controle térmico em aviários, monitorando temperatura e umidade em tempo real com painel web interativo.

## 🎯 Objetivo

Fornecer ferramenta inteligente para monitoramento ambiental em aviários:
- Redução de mortalidade por estresse térmico
- Aumento da produtividade das aves
- Tomada de decisão ágil com dados em tempo real

## 🧠 Como funciona a solução

A solução desenvolvida simula um sistema completo de Internet das Coisas (IoT) voltado para o controle térmico de aviários, integrando as três camadas clássicas da arquitetura IoT: Edge, Fog e Cloud.

**1. Camada Edge – ESP32 + DHT22**

- Um microcontrolador ESP32, equipado com um sensor DHT22, é responsável por ler continuamente a temperatura e umidade do ambiente.
Com base nessas leituras:

- Se a temperatura sair da faixa ideal (21–26 °C), um LED é acionado, simulando um alerta ou ativação de aquecedor/ventilador.

- Os dados são enviados via protocolo MQTT para um broker público (HiveMQ), representando o envio para a rede local ou nuvem.


**2. Camada Fog – Script Python com MQTT + Firebase**

- Um script Python roda localmente (no computador do operador) como ponte intermediária (Fog Computing).
Ele:
Recebe os dados MQTT enviados pelo ESP32

- Processa as leituras (ex: cálculos de média, validação, timestamp)
Envia os dados estruturados para o Firebase Firestore, armazenando cada leitura como um documento na nuvem.


**3. Camada Cloud – Dashboard Web com Streamlit**

- Um painel web, desenvolvido com Streamlit, acessa os dados diretamente do Firebase e os exibe em tempo real:

- Um gráfico temporal mostra a evolução da temperatura

- Informações como umidade atual, status (ideal, baixa, alta) e último horário de leitura são apresentadas de forma clara

- Uma tabela com histórico complementa a visualização

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

