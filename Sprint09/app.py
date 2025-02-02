import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib

# Cargar el modelo con joblib
with open('model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)  

# Cargar el OneHotEncoder entrenado
with open("scaler.pkl", "rb") as f:
    encoder = pickle.load(f)

# Título de la aplicación
st.title('Predicción de posibilidad de aceptar un depósito en un banco')

# Entrada de datos del usuario con selectbox para valores categóricos
_poutcome = st.selectbox("Previous outcome of the campaign?", ["unknown", "failure", "other", "success"])
_housing = st.radio("Do you have a house loan?", ["yes", "no"])
_contact = st.selectbox("By what means did they contact you?", ["unknown", "telephone", "cellular"])
_month = st.selectbox("In what month was the contact?", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])

# Mostrar los valores seleccionados
st.write("Selected Values:")
st.write(f"Poutcome: {_poutcome}")
st.write(f"Housing: {_housing}")
st.write(f"Contact: {_contact}")
st.write(f"Month: {_month}")

#Hacemos los mismos cambios que hicimos para entrenar el modelo
#Ojo que mes lo tenemos como estaciones
mes_a_estacion = {
    'jan': 'Winter', 'feb': 'Winter', 'dec': 'Winter',
    'mar': 'Spring', 'apr': 'Spring', 'may': 'Spring',
    'jun': 'Summer', 'jul': 'Summer', 'aug': 'Summer',
    'sep': 'Autum', 'oct': 'Autum', 'nov': 'Autum'
}
_season = mes_a_estacion[_month]

# Convertir la variable 'housing' de 'yes'/'no' a 1/0
housing_binary = 1 if _housing == 'yes' else 0

# Separar las variables que deben ser codificadas de las que no deben serlo
input_data_categorical = pd.DataFrame([[ _contact, _season, _poutcome ]], columns=['contact', 'month', 'poutcome'])
input_data_continuous = pd.DataFrame([[ _housing ]], columns=['housing'])

# Aplicar OneHotEncoding solo a las variables categóricas
input_encoded = encoder.transform(input_data_categorical)

# Convertir a un formato numérico para el modelo
input_encoded = np.array(input_encoded).reshape(1, -1)


# Concatenar las matrices, agregando 'housing_binary' directamente
input_final = np.hstack((input_encoded, input_data_continuous))

# Imprimir la forma final después de la concatenación
st.write(f"Dimensiones de input_final después de la concatenación: {input_final.shape}")


# Concatenar la variable 'housing' que no ha pasado por el encoder con las variables codificadas
#input_final = np.hstack((input_encoded, input_data_continuous))

# Realizar la predicción
prediction = model.predict(input_final)

# Mostrar la predicción
st.write(f'Predicción de la aceptación del depósito: {"Yes" if prediction[0] == 1 else "No"}')

