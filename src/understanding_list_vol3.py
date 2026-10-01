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