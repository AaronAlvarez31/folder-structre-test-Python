# Agregamos elementos a una lista

motorcycles= ["honda","mortalica","yamaha"]
print(motorcycles)

# Metodo ".append()"
"""
   El metodo '.append' ayuda a crear listas facilmente
   de manera dinamica.
"""
motorcycles.append("kawasaki")
print(motorcycles)

# Como agrgar elementos a una lista vacia
motorcycles_2 = [] # lista vacia
motorcycles_2.append("honda") # 1°elemento
motorcycles_2.append("yamaha") # 2°elemento
motorcycles_2.append("suzuki") # 3°elemento
print(motorcycles_2)

# Metodo ".insert()"
"""
   Agregas un elemento en donde tu quieras    
    Ejemplo
    motorcycles.insert('indice y elemento')
"""
motorcycles.insert(0, "ducati")      # lo pone al inicio
print(motorcycles)
motorcycles.insert(2, "bmw")         # lo pone en el indice 2
print(motorcycles)

# Metodo ".pop()"
"""
   Elimina elementos de la lista por indice.
"""
print(motorcycles)
delete_motocycke = motorcycles.pop()
print(f"Tu motocicleta borrada es: {delete_motocycke}")
print(motorcycles)
motorcycles.append(delete_motocycke)
print(motorcycles)

# Metodo ".remove()"
"""
   Elimina elementos de la lista por VALOR (no por indice).
   - Solo elimina la PRIMERA coincidencia que encuentre.
   - Si el valor no existe, lanza un ValueError.
"""
print(motorcycles)
motorcycles.remove("mortalica")
print(motorcycles)
