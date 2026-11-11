"""
#While condition
1- while infinito (while por centinela/centinel while)
Ejemplo
    while True:
        *acciones*

2- while por condicion

#Estructuras que podemos hacer con el WHile
Estructura Contadora
counter = 0
while True:
    counter = counter + 1 # o tambien como 'counter += 1'

Estructura Acumuladora
sum = 0
while True:
    sum = sum + value # o tambien como 'sum += value'
"""
#Hacer un programa que capture el importe y acumule los importes

sum = float(0.0)
message="""
    Sistema gestor de acumulacion de valores
    la creatividad esta en tus manos.
    En todo momento, siquieres salir del programa
    puedes tipear q, e, quit, exit.

Ingresar un valor numerico: """

while True:
    value_txt=input(message)
    if value_txt == "quit" or \
       value_txt == "exit" or \
       value_txt == "e" or \
       value_txt == "q":
       break
    
try:
    value=float(value_txt)
    sum= sum + value
except ValueError:
    print("Ingresaste un dato no valido")

print(f"Tu total acumulado es: {sum}")