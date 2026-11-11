"""
   Una API (Aplication Programming Interface)
   permite que 2 o mas aplicaciones intercambien informacion
   ----------        --------------
   | Python |        |  PokeAPI   |
   |        |  ----> | (servidor) |
   ----------        --------------
   Vamos a realizar nuestra primera peticion
"""
import requests
# La API corresponde a Chadizard
api_url= "https://pokeapi.co/api/v2/pokemon/6"
#Esta es la primer peticion que hacemos
response=requests.get(api_url,timeout=10)
#Para revisar si hubo errores
response.raise_for_status()
#Vamos a imprimir el codigo
print(response.status_code)
pokemon=response.json()
#Impriir info. del pokemosn
print(type(pokemon)) #dict

print("id", pokemon["id"])
print("Nombre", pokemon["name"])
print("No recuerdp", pokemon["is_default"])
print("Altura del Pokemon", pokemon["height"]/10)
print("Peso ", pokemon["weight"]/10)
for element in pokemon["types"]:
    print("Tipo", element["type"]["name"])