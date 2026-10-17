# understanding_if_statement.py
cars=["Skyline","Tsuru","Mazda","Camaro"]
for car in cars:
    if car == "Camaro":
      print(car.upper())
    else:
      print(car)
print(" ")

# El condicinal (el corazon del if)
## Para determinar igualdad ==
cookie="oreo" 
### Condiional verdadero/TRUE
print("Condicional verdadero")
print(cookie=="oreo")
print(cookie=="OREO".lower())
### Condiional falso/FALSE
print("Condicional falso")
print(cookie=="canelita")
## Para determinar desigualdad !=
### Condiional falso/FALSE en desigualdad
print("Condicional FALSE en desigualdad")
print(cookie!="oreo")
print(cookie!="OREO".lower())
### Condiional verdadero/TRUE en desigualdad
print("Condicional TRUE en desigualdad")
print(cookie!="mamut")
print(" ")

# Comparaciones numericas
print("comparaciones numericas".upper())
number=34
print(number==34) #TRUE
print(number==18) #FALSE
print(number=="34")
# Comparaciones numericas con simbolo mayor o menor que
print("comparaciones con simbolo mayor o menor que".upper())
print(number<21) #FALSE
print(number<=21) #FALSE
print(number>21) #TRUEc
print(number>=21) #TRUE

# Comparaciones con resultados
print("comparaciones con resultados")
answer=17
if answer!=42:
   print("esa no es la respuesta correcta")
print(" ")

# Ejercicio 
print("sistema de edad")
age=input("Ingresa tu edad: ")
print(type(age))
age= int(age)
print(type(age))
# Ejercicio "Costo del boleto"
if age<=4:
   cost=0
if age>4 and age<10:
   cost=200
if age>=10:
   cost=500
print("chorros de ir".upper())
print(f"El costo/precio del boleto es:{cost}")
# Ejercicio "Bloque if-elif-else"
if age <=4:
   cost=0
elif age > 4 and age <18:
   cost=200
elif age > 18 and age < 65:
   cost=500
elif age >= 65 and age <= 125:
   cost=0
elif age == 666:
   print("mero del diablo")
print("En un solo bloque".upper())
print(f"El costo/precio del boleto es:{cost}")