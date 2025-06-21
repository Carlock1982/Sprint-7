import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Panel de Control - Análisis de Vehículos")

# Cargar los datos
data = pd.read_csv("vehicles_us.csv")

# Botón para histograma
if st.button("Construir histograma de odómetro"):
    fig = px.histogram(data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button("Construir gráfico de dispersión"):
    fig_disp = px.scatter(data, x="odometer", y="price")
    st.plotly_chart(fig_disp, use_container_width=True)

