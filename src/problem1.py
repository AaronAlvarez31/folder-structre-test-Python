"""
   a) contavilizar los importes del usuario
   b) acumular los importes que ha introducido el usuario
   c) establecer el maximo y minimo de los valores introduciods
   d) calcular el promedio de los valores introducidos
   
   Despues de que el usuario decida terminar el programa
   se debe mostrar esto datos, es decir:
   I) el cntador de numero ingresado
   II) el acumulado de los numeros ingresados
   III) el promedi
   IV) el minimo valor ingresado
   V) el maximo valor ingresado
"""
listN=[]
suma=float(0.0)

while True:
    datetxt=input("Introduce un numero: ")
    date=float(datetxt)

    if date == "Exit" or "E":
        break

try:
    suma = suma + date

except ValueError:
    print("Ingresaste un dato no valido")

print(f"Tu total acumulado es: {suma}")

