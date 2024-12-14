# Tasca 4.1. Exercici 1
## Consumir una API

He escogido la API https://api.chucknorris.io/jokes/random porque es sencilla.
Lo primero ha sido instalar la biblioteca requests 
```sh
pip install requests
```

Buscamos previamente qué contiene la API. Esta en concreto tiene varias rutas, desde chistes aleatorios, categorías disponibles, etc.

Importamos las librerías
```sh

import requests
import json
```
A continuación, hacemos las peticiones a la url correspondiente
```sh
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
```
Si todo es correcto (status_code 200), podemos convertir la respuesta que nos ha dado en JSON y almacenarla.

Además, podemos hacer un control de errores un poco más exhaustivo mediante el uso de excepciones, para así tener más información sobre el tipo de error que está dando (http, tiempo de espera, conexión, etc.).
```sh
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
```
Por último, hacemos una pefición concreta.
``` sh
# Quiero un chiste de la categoría de ciencia
category = "science"  # Cambia por la categoría que quieras
url = f"https://api.chucknorris.io/jokes/random?category={category}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Chiste de la categoría {category}:", data["value"])
else:
    print("Error:", response.status_code)
```
Cuando ejecutamos el código, nos tendría que aparecer en pantalla el output adjuntado. Y además, se habrán creado dos archivos, chiste.json y categorías.json

