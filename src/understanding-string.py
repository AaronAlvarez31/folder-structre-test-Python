# STRING

"""
Un STRING es una serie de caracteres. En 
PYTHON, todo entre comillas simples '' o 
en comillas dobles "", es un STRING.

  Ejemplo:
    "Esto es un string".
    'Esto tambien es un string'
    'Le dije a un amigo, "PYTHON es mi 
    lenguaje favorito"'
    " El enguaje 'Python' es uno muy bueno"

  Ejemplo incorrecto
    (x) "Charly'
    (x) 'Charly"
"""
name = "AARON ANTONIO ALVAREZ ESCOBEDO"
name1 = "AaRoN AnToNiO AlVaReZ EsCoBeDo"
print(name)
print(name.title())
name = name.title()
print(name)

# METODOS
"""
  Los metodos es una accion que Python 
  puede realizar sobre un a variabke 
  seguido por ell nombre del metodo en
  este caso 'titlr()' dice que se tiene
  que ejecutar el metodo title() de la
  variable 'name'.

  Todos los metodos van sgudios de 
  parentesis, por esta ocasion necesita
  informacion adicional para funcionar.
  En esta casion no lo necesita.

  Ejemplos de Metodos:
    title()
    upper()
    lower()
"""
print("______________________________")
print(name1,"sin Metodos")
print(name1.title(),"Con Metodo title")
print(name1.upper(),"Con Metodo upper")
print(name1.lower(),"Con Metodo lower")