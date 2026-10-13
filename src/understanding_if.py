# understanding_if_statement.py
cars=["Skyline","Tsuru","Mazda","Camaro"]
for car in cars:
    if car == "Camaro":
      print(car.upper())
    else:
      print(car)

# El condicinal (el corazon del if)
 #Para determinar igualdad ==
cookie="oreo" 
#Condiional verdadero/TRUE
print("Condicional verdadero")
print(cookie=="oreo")
print(cookie=="OREO".lower())
#Condiional falso/FALSE
print("Condicional falso")
print(cookie=="canelita")

 #Para determinar desigualdad !=
#Condiional falso/FALSE en desigualdad
print("Condicional FALSE en desigualdad")
print(cookie!="oreo")
print(cookie!="OREO".lower())
#Condiional verdadero/TRUE en desigualdad
print("Condicional TRUE en desigualdad")
print(cookie!="mamut")

# Comparaciones numericas
print("comparaciones numericas".upper())
age=34
print(age==34) #TRUE
print(age==18) #FALSE
print(age=="34")
# Comparaciones numericas con simbolo mayor o menor que
print("comparaciones con simbolo mayor o menor que".upper())
print(age<21) #FALSE
print(age<=21) #FALSE
print(age>21) #TRUE
print(age>=21) #TRUE
print("comparaciones con resultados")
answer=17
if answer!=42:
   print("esa no es la respuesta correcta")
