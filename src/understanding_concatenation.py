# Combinacion o Conectacion de Strings

first_name = "aaron"
last_name = "alvarez"
full_name = first_name + " " + last_name
print(full_name.title())
print("hola".upper(), first_name + " " + last_name)
"""
White Space- cualquier caracter que no se imprime
(\n) para brincar un renglon
(\t) para saltar 4 espacion en el renglon
"""
print("python")
print("\tpython")
print("\t\tpython")
print("Lenguajes: \n\tPythonc\n\tC++\n\tJavaScript")

# F-Strings
famous_person = "Charly Profe"
message = f"{famous_person.upper()} una vez dijo *Python is love*"
print(message)