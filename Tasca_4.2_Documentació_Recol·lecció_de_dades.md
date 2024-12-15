# Exercici 1: Documenta el procés de recol·lecció de dades.
## 1. Fonts

**Identificació de Fonts:**
- Base de dades interna del banc IGH, recopilats com part d'una campanya de marketing cap els clients.
S'ha generat a partir de registres interns de dades telefòniques per contactar amb els clients amb l'objectiu de promocionar un producte de depòsit a llarg termini.

**Descripció de les Fonts:**
- La base de dades conté registres recolectats pel departament de marketing al banc IGH entre 2008 i 2013. 
La informació s'agrega a partir de registres de trucales i perfils financers dels clients.
Inclou dades demogràfiques (edat, ocupació, estat civil, nivell educatiu), dades financeres (saldo, crèdits pendents, historial de prèstecs), dades de contacte (canal de comunicació, duració de la trucada) i dades relacionades amb les campanyes (número de contactes realitzats, campanyes prèvies, resultats anteriors).
 
## 2. Mètodes de recol·lecció de dades

**Procediments i Eines:**
1. Registres interns del CRM del banc: les dades es registren a través del sistema CRM
2. Trucades telefòniques gravades i registrades: els detalls de les trucades es registren automàticament en eines de gestió de telefonia.
Finalment totes les dades es pugen a un sistema intern del banc. Aquesta tasca la fa el departament d'IT.

**Freqüència de Recol·lecció:**
- Es recullen en el moment de la incorporació del client i s’actualitzen periòdicament, les dades es guardaran diàriament després de cada trucada.
  
**Scripts de Descàrrega:**
Utilitzarem a API del CRM i python com a llenguatge de programació.
```python
import pandas as pd
import requests

api_url = "https://api.crm.com/dades
headers = {"Authorization": "Bearer YOUR_API_KEY"}

response = requests.get(api_url, headers=headers)
data = response.json()
df = pd.DataFrame(data)

df.to_csv("client_data.csv", index=False) # Guardar en format CSV
print("Dades descarregades i guardades amb èxit.")

print(df.info())
```

## 3. Format i Estructura de les Dades

**Tipus de Dades:**
- Numèriques:
-`age`: Edat del client (numèrica contínua).
-`balance`: Saldo mitjà anual del client en euros (numèrica contínua).
-`day`: Dia del mes en què es va realitzar el contacte (numèrica discreta).
-`duration`: Durada de la trucada telefònica en segons (numèrica contínua).
-`campaign`: Nombre de contactes realitzats durant la campanya actual (numèrica discreta).
-`pdays`: Nombre de dies des de l’últim contacte en una campanya anterior (numèrica discreta; -1 si no s’ha contactat abans).
-`previous`: Nombre de contactes realitzats en campanyes anteriors (numèrica discreta) 

- Categòriques:
-`job`: Ocupació del client.
-`marital`: Estat civil del client.
-`education`: Nivell educatiu del client.
-`default`: Si el client té crèdits pendents.
-`housing`: Si el client té un préstec hipotecari.
-`loan`: Si el client té un préstec personal.
-`contact`: Tipus de contacte utilitzat.
-`month`: Mes en què es va realitzar el contacte.
-`poutcome`: Resultat d’una campanya de màrqueting anterior.
-`deposit`: Variable objectiu que indica si el client va contractar el dipòsit.

**Format d'Emmagatzematge:**
- Emmagatzematge en fitxer CSV perquè les dades són tabulars i no tenen relacions complexes entre camps. A més, es pot fer un anàlisi senzill amb programació.

## 4. Limitacions de les dades

- Diferents temps d'actualització: Les interaccions telefòniques i saldos financers poden ser actualitzats en moments diferents.
- Qualitat i exhaustivitat de les dades categòriques: algunes variables tenen valors "unknown", que són incompletes.
- Dades obsoletes: si fa molt de temps des l'última campanya, algunes variables poden no ser rellevants, com pdays o previous.
- Simplificació de les interaccions: La durada és l'únic indicador de l'eficàcia del contacte, però no hi ha informació qualitativa sobre el contingut de la interacció o la resposta del client.

## 5. Consideracions sobre Dades Sensibles

**Tipus de Dades Sensibles:**
- Informació Personal Identificable (PII): `age`, `job`, `marital`, `education`
- Informació Financera Sensible: `balance`, `default`, `housing`, `loan` 
- Dades Comportamentals Sensibles. Les podem separar entre: 
	- Dades de contacte i interacció que donen informació sobre els canals i moments de contacte: `contact`, `duration`, `day`, `month` 
	- Resultats de campanyes que poden relevar comportament del client: `poutcome`, `previous`, `campaing`, `deposit`

**Mesures de Protecció:**
- **Anonimització i Pseudonimització:**
  - Es poden transformar dades personal que identifiquin directament un individu (ex. edat per intervals), o substituir valors identificables per codi (job per identificador numèric)
- **Minimització de dades:**
  - Recollit només les dades necessàries per l'objectiu
- **Xifrat de dades:**
  - Camps sensibles com balance o default
- **Accés Restringit:**
  - Limitar l’accés a les dades als usuaris autoritzats mitjançant sistemes de control d’accés.
- **Auditoria i Compliment normatiu:**
  - Implementar registres d'auditoria i compliment amb la GDRP
