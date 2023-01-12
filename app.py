import streamlit as st
import pandas as pd
import numpy as np
import joblib

import pandas as pd
import numpy as np

def relu(x):
  return np.maximum(0, x)

def sig(x):
 return 1/(1 + np.exp(-x))

def hip(x):
  return np.tanh(x)

class Neuron():
  def __init__(self,weights, bias, func):
    self.weights = weights
    self.bias = bias
    self.func = func

  def changebias(self,bias):
    self.bias = bias

  def changeweights(self,weights):
    self.weights = weights
    
  def run(self, input_data):
    x = np.array(input_data)
    calc = np.dot(self.weights, x) + self.bias
    if self.func == "ReLu":
      self.func = relu
    elif self.func == "Sigmoide":
      self.func = sig
    elif self.func == "Tangente Hipervolica":
      self.func = hip
    return self.func(calc)
st.image("neurona.jpg", width=450)
st.title("Simulador de neurona")

c = st.slider("Indica el numero de entradas y pesos:",0.0, 5.0)
input_numbers = []
for i in range(c):
  input_numbers.append(st.number_input(f"w{i}", step = 0.01))


st.title("¡Entradas!")
x = st.number_input("Entrada x")

st.title("¡Pesos!")
weights = st.number_input("Entrada w")

col1, col2 = st.columns(2)
with col1:
  bias = st.number_input("Introduzca el valor del sesgo")
with col2:
  func = st.selectbox('Selecciona funcion de activacion',("Sigmoide", "ReLu", "Tangente Hipervolica" ))
      
if st.button("Calcular la salida"):
  miNeurona = Neuron(weights, bias, func)
  output = miNeurona.run(input_data = x)
  st.text(output)
