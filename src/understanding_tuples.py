"""
   Tuplas: listas de elementos que no cambian de tamaño,
           son listas inmutables. Se utilizan los () para
           definir una tupla.
"""
dimensions=(200,50) #200 de ancho * 50 de largo
print("tupla original",dimensions)
print(dimensions[0])
print(dimensions[1])

#Vamos a modificar el valor de una lista
names=["carlos","charly","juan","wendy","papoy"]
print(names)
names[0]="mercury"
names[1]="mercury"
names[2]="mercury"
print(names)

#dimensions[0]=500 #Esta operacion no esta permitida

#Looping trogh a tuple
for dimension in dimensions:
    print(dimension)
"""
   No podemos modificar una TUPLA, pero si cambiar la
   asignacion de una variable.
"""
dimensions=(500,1000,20)
print("tupla re-definida",dimensions)

#Tipos de datos Booleanos
"""
   Electronica Electricidad Logica Programacion
       off          0v        0       False
       ON           5v        1       True
"""
answer=True
print(answer)
answer2=False
print(answer2)
#print(dir(answer))