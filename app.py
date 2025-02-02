import streamlit as st
import pickle
import pandas as pd

# Cargar el modelo y el escalador desde archivos
with open('my_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

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
    'Jan': 'Winter', 'Feb': 'Winter', 'Dec': 'Winter',
    'Mar': 'Spring', 'Apr': 'Spring', 'May': 'Spring',
    'Jun': 'Summer', 'Jul': 'Summer', 'Aug': 'Summer',
    'Sep': 'Autum', 'Oct': 'Autum', 'Nov': 'Autum'
}
_season = mes_a_estacion[_month]

# Cargar el OneHotEncoder entrenado (guárdalo en un archivo .pkl cuando entrenes tu modelo)
with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

input_data = pd.DataFrame([[ _contact, _season, _poutcome ]], columns=['contact', 'month', 'poutcome'])

# Aplicar OneHotEncoding a los datos de entrada
input_encoded = encoder.transform(input_data)

# Convertir a un formato numérico para el modelo
input_encoded = np.array(input_encoded).reshape(1, -1)

# Mostrar resultados codificados
st.write("Categorical features transformed:", input_encoded)

# Crear un DataFrame con las entradas
user_data = pd.DataFrame({
    'Length of Membership': [length_of_membership],
    'Time on App': [time_on_app],
    'Avg. Session Length': [avg_session_length]
})

# Realizar la predicción
prediction = model.predict(user_data)

# Mostrar la predicción
st.write(f'Predicción del aceptación del depósito: {prediction[0]:.2f}')

