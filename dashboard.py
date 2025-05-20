# dashboard.py
import streamlit as st
import time
import pandas as pd
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase
cred = credentials.Certificate("aula-pos-iot-firebase-adminsdk-fbsvc-83d07bc95e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

st.set_page_config(page_title="Monitor Aviário", layout="centered")
st.title("🐔 Termômetro do Aviário - Dashboard")

status_box = st.empty()
timestamp_box = st.empty()
grafico = st.empty()
tabela = st.empty()

leituras_temp = []

ultima_lida = None

while True:
    try:
        # Buscar último documento
        docs = db.collection("leituras_aviario") \
                 .order_by("timestamp", direction="DESCENDING") \
                 .limit(1).stream()

        doc = next(docs, None)
        if doc:
            dados = doc.to_dict()
            if dados != ultima_lida:
                ultima_lida = dados

                temperatura = dados["temperatura"]
                umidade = dados["umidade"]
                status = dados["status"]
                timestamp = dados["timestamp"]

                # Armazenar com timestamp real
                leituras_temp.append({
                    "Timestamp": timestamp,
                    "Temperatura (°C)": temperatura,
                    "Umidade (%)": umidade,
                    "Status": status
                })
                if len(leituras_temp) > 20:
                    leituras_temp.pop(0)

                # Atualizar status
                status_box.info(
                    f"📣 {status} | 🌡️ **{temperatura:.1f}°C** | 💧 **{umidade:.1f}%**"
                )
                timestamp_box.markdown(f"🕒 Última leitura recebida: **{timestamp}**")

                # Criar DataFrame com as últimas leituras
                df = pd.DataFrame(leituras_temp)
                df["Timestamp"] = pd.to_datetime(df["Timestamp"], format="%d/%m/%Y %H:%M:%S")

                # Gráfico com eixo X temporal
                grafico.line_chart(df.set_index("Timestamp")[["Temperatura (°C)"]])

                # (Opcional) Mostrar tabela abaixo do gráfico
                tabela.dataframe(df[::-1], use_container_width=True)

        time.sleep(5)

    except Exception as e:
        st.warning("Erro ao buscar dados do Firebase.")
        st.text(str(e))
        time.sleep(5)