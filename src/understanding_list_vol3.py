# Trabajando con listas

print("\n\tTrabajajaremos con listas hoy".upper())

print("-------------------Imprimiendo a la mala")
magicians=["harry","ron","hermione","snape","lupin"]
print(magicians[0], magicians[1],magicians[2], magicians[3],magicians[4])

# Ciclo for
print("-------------------Imprimiendo con for")
for magician in magicians:
 # 'print(magician)'asi se imprime y hace un salto
    print(magician, end=" ") # asi se imprime pero borra ese salto y pone un espacio
print("\n")

print("-------------------Imprimiendo con for con catenacion de strings")
# Clico for con catenacion de strings
for magician in magicians:
    print(f"{magician.title()} ese fue un buen hechizo.")
    print(f"No puedo esperar al siguiente, {magician.upper()}\n")
print("Gracias por el show")

# Identacion
"""
Pytho utiliza la identacion para determinar
cuando na linea de codigo esta conectada a la
linea de codigo anterior.
Se utilizan 4 espacios en blanco para obligarnos 
a escribir codigo ordenado y estructurado.
"""
#No olvidemos identar Traceback IdentationError
players = ["lucy", "rebeca", "david"]
#Error de Logica
for player in players:
    print(player)
print(f"Algunos de ellos siguen vivos{player.title()}")