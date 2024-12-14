'''
API
(1) Instalamos la biblioteca request
(2) Buscamos previmanete qué contiene la API. Esta en concreto tiene varias rutas, desde chistes aleatorios, categorías disponibles, etc.
(3) Hacemos peticiones
(4) Hacemos control de errores
'''

import requests
import json

# Quiero obtener un chiste aleatorio
url = "https://api.chucknorris.io/jokes/random"

# Hacer una solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue OK (código 200)
if response.status_code == 200:
    data = response.json()  # Convertir respuesta a JSON
    print("Chiste:", data["value"])
    # Ahora guardamos la información obtenida
    with open("chiste.json", "w") as file:
        json.dump(data, file, indent=4)  # Guardar con formato bonito
    print("Chiste guardado en 'chiste.json'")
else:
    print("Error:", response.status_code)

# Quiero saber qué categorías están disponibles y quiero añadir un control de errores más estricto
url = "https://api.chucknorris.io/jokes/categories"

try:
    response = requests.get(url) # Solicitud GET
    response.raise_for_status()  # Lanza una excepción si hay un error HTTP

    # Verificar que la solicitud fue OK (código 200)
    data = response.json()  # Convertir respuesta a JSON
    print("Categorías:", data)
    
    # Ahora guardamos la información obtenida
    with open("categorías.json", "w") as file:
        json.dump(data, file, indent=4)  # Guardar con formato bonito
    print("Categorías guardadas en 'categorías.json'")

except requests.exceptions.HTTPError as errh:
    print("Error HTTP:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error de conexión:", errc)
except requests.exceptions.Timeout as errt:
    print("Error de tiempo de espera:", errt)
except requests.exceptions.RequestException as err:
    print("Error inesperado:", err)
except Exception as e:
    print("Ha ocurrido un error inesperado:", e)


# Quiero un chiste de la categoría de ciencia
category = "science"  # Cambia por la categoría que quieras
url = f"https://api.chucknorris.io/jokes/random?category={category}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Chiste de la categoría {category}:", data["value"])
else:
    print("Error:", response.status_code)


