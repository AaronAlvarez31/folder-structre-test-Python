# PORTADA
"""
   Name: Aaron Antonio Alvarez Escobedo
   Student ID: 2630437
   Group: 1-1
   Subject: Metodologias de la programacion
   Professor: M.C. CARLOS ANTONIO TOVAR GARCIA
   Date: 18/10/26
"""
# RESUMEN EJECUTIVO
"""
   En Python, una lista es una coleccion ordenada y mutable de
   elementos, una tupla es una coleccion ordenada pero inmutable,
   y un diccionario es una coleccion de pares clave-valor. Que una
   lista sea mutable significa que se puede modificar (agregar,
   eliminar, cambiar elementos); una tupla no se puede modificar
   despues de creada. Los diccionarios asocian claves con valores,
   lo que permite buscar informacion rapidamente por una clave
   (por ejemplo, un nombre o un id). Este documento presenta 6
   problemas resueltos con listas, tuplas y diccionarios, cada uno
   con descripcion, entradas, salidas, validaciones, casos de
   prueba y su codigo.
"""
# PRINCIPIOS Y BUENAS PRACTICAS
"""
   - Usar listas cuando se necesite agregar o eliminar elementos
     con frecuencia.
   - Usar tuplas para datos que no deben cambiar (por ejemplo,
     coordenadas, fechas, configuraciones fijas).
   - Usar diccionarios cuando se necesite buscar informacion por
     una clave (por ejemplo, por nombre, id, codigo).
   - Evitar modificar una lista mientras se recorre con un for,
     a menos que se sepa exactamente lo que se hace.
   - Usar nombres de claves descriptivos en los diccionarios
     (por ejemplo, "name", "age", "price").
   - Escribir codigo legible y mensajes claros para el usuario.
"""

# Problem 1: Shopping list basics (list operations)
"""
Description:
   Reads a comma-separated list of products, cleans spaces,
   adds a new product, and checks if a search product is in
   the list.

Inputs:
   - initial_items_text (string)
   - new_item (string)
   - search_item (string)

Outputs:
   - "Items list: <items_list>"
   - "Total items: <len_list>"
   - "Found item: true|false"

Validations:
   - initial_items_text must not be empty after strip().
   - new_item and search_item must not be empty.

Test cases:
   1) Normal: "apple,banana,orange", "grape", "banana"
              -> list with 4 items, found = True
   2) Border: "apple", "banana", "apple"
              -> list with 2 items, found = True
   3) Error:  "", "grape", "banana"
              -> "Error: invalid input"
"""

items=input("Enter list products: ")
strip_items=items.strip()
list_items=strip_items.split(",")
clean_list = []

if strip_items == "":
    print("Error: invalid input")
else:
    for item in list_items:
        clean_list.append(item.strip())

new_item=input("Enter new product: ")
strip_new=new_item.strip()
if strip_new=="":
   print("Error: invalid input")
else:
    clean_list.append(strip_new)

search_item = input("Enter product to search: ")
strip_search = search_item.strip()
if strip_search == "":
    print("Error: invalid input")
else:
    found = strip_search in clean_list
    print(f"Items list: {clean_list}")
    print(f"Total items: {len(clean_list)}")
    print(f"Found item: {found}")

# Problem 2: Points and distances with tuples
"""
Description:
   Reads four coordinates, builds two tuples (point_a, point_b),
   calculates the Euclidean distance between them, and builds
   a midpoint tuple.

Inputs:
   - x1, y1, x2, y2 (float)

Outputs:
   - "Point A: (x1, y1)"
   - "Point B: (x2, y2)"
   - "Distance: <distance>"
   - "Midpoint: (mx, my)"

Validations:
   - All four inputs must be convertible to float.

Test cases:
   1) Normal: 0, 0, 3, 4     -> distance 5.0, midpoint (1.5, 2.0)
   2) Border: 1, 1, 1, 1     -> distance 0.0, midpoint (1.0, 1.0)
   3) Error:  "a", 0, 3, 4   -> "Error: invalid input"
"""
print("Enter 4numbers")
n0=input("Number1:")
n1=input("Number2:")
n2=input("Number3:")
n3=input("Number4:")

try:
    x1=float(n0)
    y1=float(n1)
    x2=float(n2)
    y2=float(n3)

    point_a=(x1,y1)
    point_b=(x2,y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")

except ValueError:
    print("Error: invalid input")

# Problem 3: Product catalog with dictionary
"""
Description:
   Manages a small product catalog stored in a dictionary
   (name -> unit price). Reads a product name and a quantity,
   and calculates the total price if the product exists.

Inputs:
   - product_name (string)
   - quantity (int)

Outputs:
   - If the product exists:
       "Unit price: <unit_price>"
       "Quantity: <quantity>"
       "Total: <total_price>"
   - If not:
       "Error: product not found"

Validations:
   - product_name must not be empty after strip().
   - quantity must be a positive integer.
   - product_name must be a key in the dictionary.

Test cases:
   1) Normal: "apple", 3      -> unit 10.0, total 30.0
   2) Border: "banana", 1     -> unit 5.5, total 5.5
   3) Error:  "grape", 2      -> "Error: product not found"
"""

product_prices = {
    "apple": 10.0,
    "banana": 5.5,
    "orange": 8.0
}

product_name = input("Name product: ")
strip_name = product_name.strip()

if strip_name == "":
    print("Error: invalid input")
else:
    try:
        quantity = int(input("Amount product: "))

        if quantity <= 0:
            print("Error: invalid input")
        elif strip_name in product_prices:
            unit_price = product_prices[strip_name]
            total = unit_price * quantity
            print(f"Unit price: {unit_price}")
            print(f"Quantity: {quantity}")
            print(f"Total: {total}")
        else:
            print("Error: product not found")

    except ValueError:
        print("Error: invalid input")

# Problem 4: Student grades with dict and list
"""
Description:
   Manages student grades using a dictionary where each key
   is a student name and each value is a list of grades.
   Reads a student name, calculates the average, and tells
   if the student passed (average >= 70.0).

Inputs:
   - student_name (string)

Outputs:
   - If the student exists:
       "Grades: <grades_list>"
       "Average: <average>"
       "Passed: true|false"
   - If not:
       "Error: student not found"

Validations:
   - student_name must not be empty after strip().
   - student_name must be a key in the dictionary.
   - The grades list must not be empty before averaging.

Test cases:
   1) Normal: "alice"  -> grades [90, 85], average 87.5, passed True
   2) Border: "bob"    -> grades [70], average 70.0, passed True
   3) Error:  "zoe"    -> "Error: student not found"
"""

PASSING_GRADE = 70.0

grades = {
    "alice": [90, 85],
    "bob": [70],
    "charlie": [60, 65, 55]
}

student_name = input("Enter student name: ")
strip_name = student_name.strip().lower()

if strip_name == "":
    print("Error: invalid input")
elif strip_name in grades:
    student_grades = grades[strip_name]

    if len(student_grades) == 0:
        print("Error: invalid input")
    else:
        average = sum(student_grades) / len(student_grades)

        if average >= PASSING_GRADE:
            is_passed = True
        else:
            is_passed = False

        print(f"Grades: {student_grades}")
        print(f"Average: {average}")
        print(f"Passed: {is_passed}")
else:
    print("Error: student not found")

# Problem 5: Word frequency counter (list + dict)
"""
Description:
   Reads a sentence, converts it to lowercase, splits it into
   words, builds a frequency dictionary, and shows the most
   common word.

Inputs:
   - sentence (string)

Outputs:
   - "Words list: <words_list>"
   - "Frequencies: <freq_dict>"
   - "Most common word: <word>"

Validations:
   - sentence must not be empty after strip().
   - The words list must not be empty.

Test cases:
   1) Normal: "the cat and the dog" -> most common "the"
   2) Border: "hello"               -> most common "hello"
   3) Error:  ""                    -> "Error: invalid input"
"""

sentence = input("Enter a sentence: ")
strip_sentence = sentence.strip().lower()

if strip_sentence == "":
    print("Error: invalid input")
else:
    clean_sentence = strip_sentence.replace(".", "")
    clean_sentence = clean_sentence.replace(",", "")
    words_list = clean_sentence.split()

    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] = freq_dict[word] + 1
            else:
                freq_dict[word] = 1

        most_common_word = ""
        max_freq = 0

        for word in freq_dict:
            if freq_dict[word] > max_freq:
                max_freq = freq_dict[word]
                most_common_word = word

        print(f"Words list: {words_list}")
        print(f"Frequencies: {freq_dict}")
        print(f"Most common word: {most_common_word}")

# Problem 6: Simple contact book (dictionary CRUD)
"""
Description:
   Implements a mini contact book using a dictionary
   (name -> phone). Reads an action ("ADD", "SEARCH" or
   "DELETE") and performs the corresponding operation.

Inputs:
   - action_text (string)
   - name (string)
   - phone (string, only for ADD)

Outputs:
   - ADD:    "Contact saved: <name>, <phone>"
   - SEARCH: "Phone: <phone>" or "Error: contact not found"
   - DELETE: "Contact deleted: <name>" or "Error: contact not found"

Validations:
   - action_text must be one of "ADD", "SEARCH", "DELETE".
   - name must not be empty after strip().
   - For ADD: phone must not be empty after strip().

Test cases:
   1) Normal: "ADD", "diana", "5551234"
              -> "Contact saved: diana, 5551234"
   2) Border: "SEARCH", "alice"   -> "Phone: 1234567890"
   3) Error:  "SEARCH", "zoe"     -> "Error: contact not found"
"""

contacts = {
    "alice": "1234567890",
    "bob": "0987654321"
}

action_text = input("Enter action (ADD/SEARCH/DELETE): ")
action = action_text.strip().upper()

if action == "ADD":
    name = input("Enter contact name: ")
    strip_name = name.strip().lower()

    if strip_name == "":
        print("Error: invalid input")
    else:
        phone = input("Enter phone: ")
        strip_phone = phone.strip()

        if strip_phone == "":
            print("Error: invalid input")
        else:
            contacts[strip_name] = strip_phone
            print(f"Contact saved: {strip_name}, {strip_phone}")

elif action == "SEARCH":
    name = input("Enter contact name: ")
    strip_name = name.strip().lower()

    if strip_name == "":
        print("Error: invalid input")
    elif strip_name in contacts:
        print(f"Phone: {contacts[strip_name]}")
    else:
        print("Error: contact not found")

elif action == "DELETE":
    name = input("Enter contact name: ")
    strip_name = name.strip().lower()

    if strip_name == "":
        print("Error: invalid input")
    elif strip_name in contacts:
        contacts.pop(strip_name)
        print(f"Contact deleted: {strip_name}")
    else:
        print("Error: contact not found")

else:
    print("Error: invalid input")

# CONCLUSIONES
"""
   Las listas, tuplas y diccionarios son estructuras fundamentales
   en Python. Las listas convienen cuando se necesita agregar o
   eliminar elementos de forma flexible, como en una lista de
   compras o un catalogo. Las tuplas son utiles para datos que no
   deben cambiar, como coordenadas o registros fijos. Los
   diccionarios facilitan busquedas rapidas por clave, como
   nombres de estudiantes, productos o contactos. Combinar estas
   estructuras (por ejemplo, un diccionario de listas para
   calificaciones) permite modelar datos del mundo real de forma
   clara y eficiente.
"""
# REFERENCES
"""
   1) Python documentation - Built-in Types: list, tuple, dict.
      https://docs.python.org/3/library/stdtypes.html
   2) Python documentation - Data Structures Tutorial.
      https://docs.python.org/3/tutorial/datastructures.html
   3) W3Schools - Python Lists, Tuples, Dictionaries.
      https://www.w3schools.com/python/
   4) Real Python - Python Dictionaries.
      https://realpython.com/python-dicts/
   5) GeeksforGeeks - Python Data Structures.
      https://www.geeksforgeeks.org/python-data-structures/
"""