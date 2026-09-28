"""
   Una lista nos permkte almacernar informacion
   en un lugar, la cantiddad que se desee: ya
   sean pocos elementos o millones de elementos.

   Una lista es una coleccion de items (elementos) que 
   tiene un orden particular. Se pueden crear listas que
   incluyan strings, enteros, floats, los nombres de las 
   personas de tu facilidad, etc.
   Podemos almacernar "los tipos de datos permitidos en 
   Python" lo que queremos en un lista.

   Son elementos Mutables: pueden modificarse su tamaño de
   la lista.

   Se recomienda nombrar una variable de tipo lista, sus
   elementos se separan por comas.

     EJEMPLO
"""

bicycles = "trak", "cannondable", "redline", "specialized", "apache"
print(bicycles)

# Como se accede a los elementos de una lista?
"""
   Las listas son colecciones ordenadas. Se puede acceder
   a un elemento de una lista diciendole a Python la
   posicion o indice del elemento deseado.

   Para obtener el valor desea, se debe escribir el 
   nombre de la lsita, seguido del indice del elemento
   entre corchetes.
"""
print(bicycles[0], bicycles[1], bicycles[2])
print(bicycles[0].upper())

# Accediendo desde el ultimo elemento de la lista.

print(bicycles[-1]) # apache
print(bicycles[-2]) # specialized

# Utilizando valores individuales de una lista.
message = f"My first bicycle was a {bicycles[-1].upper()}"
print(message)

