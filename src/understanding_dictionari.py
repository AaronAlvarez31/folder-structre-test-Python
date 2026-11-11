# Diccionario Simple
alien0={"","",""}


alien2={
    "":"",
    }




"""
   NESTING
   1- Lista de diccionarios
   2- Listas en diccionarios
   3- Diccionario de diccionarios

"""
elites={
    "name":"elite",
    "color":"blue",
    "points":"qo",
    "shield":True
}
jackals={
    "name":"jackal",
    "color":"gray",
    "points":"6",
    "shield":True,
}
grunts={
    "name":"grunt",
    "color":"orange",
    "points":"3",
    "shield":False
}
covenants=[]
covenants.append(grunts)
covenants.append(jackals)
covenants.append(elites)

print("Looping")
for covenant in covenants:
    print(covenant)

covenants_fleet=[]
for _ in range(2):
    covenants_fleet.append(co)
