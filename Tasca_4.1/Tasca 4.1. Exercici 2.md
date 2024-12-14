# Tasca 4.1. Exercici 2
## Obtenir dades amb Web Scraping

He escogido la página web de Amazon porque es conocida y se puede extraer y recopilar esos datos disponibles de forma gratuita sin infringir los términos de servicio de Amazon. En concreto, he utilizado la URL de un árbol de Navidad con legos.

Lo primero ha sido instalar la biblioteca requests y beautifulsoup4
```sh
pip install requests beautifulsoup4
```

Buscamos previamente qué contiene la página web, que vende un producto.

Importamos las librerías
```sh
import requests
from bs4 import BeautifulSoup
import random
import time
```
A continuación, simulamos un User-Agent para evitar ser bloqueados y hacemos las peticiones a la url correspondiente.
```sh

# URL del producto en Amazon.es (ejemplo: un árbol de Navida de legos)
url = "https://www.amazon.es/LEGO-%C3%81rbol-de-Navidad-40573/dp/B0BCP2HHBC?pd_rd_w=Hq6RP&content-id=amzn1.sym.99372bbf-8dd0-4fda-9ccf-78db539c0b30&pf_rd_p=99372bbf-8dd0-4fda-9ccf-78db539c0b30&pf_rd_r=6YEZDJEYMYNYTHM1367Q&pd_rd_wg=ECFuj&pd_rd_r=4372ffb0-63d2-4ffe-9093-e76ac2a26559&pd_rd_i=B0BCP2HHBC&ref_=xmas_advent_eu5_0_B0BCP2HHBC"

# Simulación de un User-Agent para evitar ser bloqueado
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}
```

A continuación, hacemos las peticiones a la url correspondiente
``` sh
try:
    # Hacer la solicitud GET
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Errores

    # Analizar el contenido HTML con BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")
``` 
Buscaremos información sobre el título del producto, precio y valoraciones.
``` sh
    # TÍTULO
    title = soup.find("span", id="productTitle")
    if title:
        title = title.get_text(strip=True)
    else:
        title = "No se ha encontradoo"

    # PRECIO
    price = soup.find("span", class_="a-price-whole")
    if price:
        price = price.get_text(strip=True)
    else:
        price = "No se encontró el precio"

    # RESEÑAS
    reviews = soup.find("span", class_="a-icon-alt")
    if reviews:
        reviews = reviews.get_text(strip=True)

    # Imprimir los datos
    print(f"Título: {title}")
    print(f"Precio: {price}")
    print(f"Reseñas: {reviews}")
```
Además, podemos hacer un control de errores un poco más exhaustivo mediante el uso de excepciones, para así tener más información sobre el tipo de error que está dando.
``` sh
except requests.exceptions.HTTPError as errh:
    print("Error HTTP:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Error de conexión:", errc)
except requests.exceptions.Timeout as errt:
    print("Error de tiempo de espera:", errt)
except requests.exceptions.RequestException as err:
    print("Error inesperado:", err)
```
