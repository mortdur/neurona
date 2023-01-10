import streamlit as st
import pandas as pd
import joblib
st.image("neurona.jpg", width=450)
st.title("¡Hola neurona!")
tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entrada y sesgo"])

with tab1:
  st.title("Una neurona con una entrada y un peso")
  x = st.slider("Peso:",0.0, 5.0)
  w = st.number_input("Valor de entrada")
  if st.button("Calcular la salida",key="boton1"):
    y = x * w
    st.text(f"Resultado {y}")

with tab2:
  col1, col2 = st.columns(2)
  with col1:
    x0 = st.slider("Peso w0:",0.0, 5.0,key="x0")
    w0 = st.number_input("Entrada x0",key="w0")
  with col2:
    x1 = st.slider("Peso w0:",0.0, 5.0,key="x1")
    w1 = st.number_input("Entrada x1",key="w1")
    if st.button("Calcular la salida",key="salida2"):
      y = x0 * w0 + x1 * w1
      st.text(f"Resultado {y}")

with tab3:
  col1, col2, col3 = st.columns(3)
  with col1:
    x0 = st.slider("Peso w0:",0.0, 5.0,key="x00")
    w0 = st.number_input("Entrada x0",key="w00")
    b = st.number_input("Introduzca el valor del sesgo")
  with col2:
    x1 = st.slider("Peso w1:",0.0, 5.0,key="x01")
    w1 = st.number_input("Entrada x1",key="w01")
  with col3:
    x2 = st.slider("Peso w2:",0.0, 5.0,key="x02")
    w2 = st.number_input("Entrada x2",key="w02")
    if st.button("Calcular la salida",key="salida3"):
      y = x0 * w0 + x1 * w1 + x2 * w2 + b
      st.text(f"Resultado {y}")