players= ["peter","mercado","aaron","fatima","itace"]
print("Lista original", players)

#slicing
print(players[3:5]) 
print(" ") 

print("1:4",players[1:4]) 
print(" :3",players[:3]) 
print("2: ",players[2:]) 
print("-3:",players[-3:]) 
print("uno",players[0]) 

print("\nCasos especiales")
print(players)
print(players[1:10])
print(players[-10:10])
print(players[6:1])
print(players[:0])
print(players[0:1])

# Loping de un slicing
print("\nLoping usando slicing")
peoples=["peter","mercado","aaron","fatima","itace"]
for people in peoples[3:5]:
    print(f"El estudiante {people}, va a pasar la materia")
print(people,"\n")

# Como copiar una lista?
myfood=["enchiladas","cheesecake","discada","flautas"]
#'friendfood=myfood' seria la Manera erronea de copiar listas

#3aneras de copiarlo correctamente

#usar slicing
friendfood=myfood[:]
print(friendfood)
#usando metodo de lista: .copy()
friendfood1=myfood.copy()
print(friendfood1)
#usando metodo lista build-in: list()
friendfood2=list(myfood)
print(friendfood2)