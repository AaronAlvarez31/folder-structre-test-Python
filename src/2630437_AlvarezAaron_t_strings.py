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
   En Python, un string es una secuencia de caracteres encerrada
   entre comillas simples o dobles. Los strings son inmutables:
   cualquier operacion que los modifique genera una nueva cadena,
   no altera la original. Con ellos se pueden concatenar textos,
   obtener su longitud con len(), extraer subcadenas con slicing,
   buscar patrones con in / find(), y reemplazar texto con
   replace(). Tambien se pueden dividir con split() y unir con
   join(). Validar y normalizar el texto de entrada (con strip()
   y lower()) es esencial para evitar datos basura, comparar
   correctamente y procesar entradas de usuario como correos,
   nombres o contrasenas. Este documento presenta 6 problemas
   resueltos con strings, cada uno con descripcion, entradas,
   salidas, validaciones, casos de prueba y su codigo.
"""
# PRINCIPIOS Y BUENAS PRACTICAS
"""
   - Los strings son inmutables: cualquier cambio genera una
     nueva cadena.
   - Es buena practica normalizar la entrada con strip() y
     lower() antes de compararla.
   - Evitar "numeros magicos" en indices; documentar que extrae
     cada slice.
   - Usar metodos de string en lugar de reescribir logica basica.
   - Disenar validaciones claras: primero que no este vacio,
     luego el formato.
   - Escribir codigo legible: nombres de variables claros y
     mensajes de error entendibles.
"""

# Problem 1: Full name formatter (name + initials)
"""
 Description:
Reads a full name, normalizes spaces and letter case, shows
it in Title Case, and builds the initials with periods.
Example: "juan carlos tovar" -> "Juan Carlos Tovar" / "J.C.T."

 Inputs:
- full_name (string)

 Outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

 Validations:
- full_name must not be empty after strip().
- Must contain at least two words.
- Strings with only spaces are rejected.

 Test cases:
1) Normal: "juan carlos tovar" -> "Juan Carlos Tovar", "J.C.T."
2) Border: "  ana   lopez  " -> "Ana Lopez", "A.L."
3) Error:  "" -> "Error: invalid input"
"""

MIN_WORDS = 2

full_name = input("Enter your full name: ")

# clean spaces
clean_name = full_name.strip()
name_parts = clean_name.split()
name_words = " ".join(name_parts)

# validate not empty
if name_words == "":
    print("Error: invalid input")
else:
    # validate at least two words
    if len(name_parts) < MIN_WORDS:
        print("Error: name must have at least two words")
    else:
        # formatted name
        formatted_name = name_words.title()

        # build initials
        initials = ""
        for word in name_parts:
            initials += word[0].upper() + "."

        # show results
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")

# Problem 2: Simple email validator (structure + domain)
"""
Description:
Reads an email address and checks a basic valid format:
exactly one '@', at least one '.' after the '@', and no
spaces. If valid, it also shows the domain part.

Inputs:
- email_text (string)

Outputs:
- "Valid email: true"  or  "Valid email: false"
- If valid: "Domain: <domain_part>"

Validations:
- email_text must not be empty after strip().
- Must contain exactly one '@'.
- Must not contain spaces.
- The part after '@' must contain at least one '.'.

Test cases:
1) Normal: "user@example.com" -> "Valid email: true", "Domain: example.com"
2) Border: "user@example" -> "Valid email: false"
3) Error:  "user example.com" -> "Valid email: false"
"""

email_text = input("Enter your email: ")
clean_email_text = email_text.strip()

if clean_email_text == "":
    print("Error: invalid input")
else:
    at_count = clean_email_text.count("@")

    if at_count != 1:
        print("Valid email: false")
    elif " " in clean_email_text:
        print("Valid email: false")
    else:
        at_position = clean_email_text.find("@")
        domain = clean_email_text[at_position + 1:]

        if "." not in domain:
            print("Valid email: false")
        else:
            print("Valid email: true")
            print(f"Domain: {domain}")

# Problem 3: Palindrome checker (ignoring spaces and case)
"""
Description:
Reads a phrase and checks if it is a palindrome, that is,
it reads the same forwards and backwards, ignoring spaces
and uppercase/lowercase differences.

Inputs:
- phrase (string)

Outputs:
- "Is palindrome: true"  or  "Is palindrome: false"

Validations:
- phrase must not be empty after strip().
- Minimum length of 3 characters after removing spaces.

Test cases:
1) Normal: "Anita lava la tina" -> "Is palindrome: true"
2) Border: "a"                  -> "Is palindrome: false"
3) Error:  ""                   -> "Error: invalid input"
"""

palindrome = input("Please enter a palindrome: ")
strip_palindrome = palindrome.strip()
lower_palindrome = strip_palindrome.lower()
clean_palindrome = lower_palindrome.replace(" ","")
check_palindrome = clean_palindrome[ : :-1]

if clean_palindrome == "":
    print("Error: invalid input")
elif len(clean_palindrome) < 3:
    print("Is palindrome: false")
else:
    if clean_palindrome == check_palindrome:
        print("Is palindrome: true")
    else:
        print("Is palindrome: false")

# Problem 4: Sentence word stats (lengths and first/last word)
"""
Description:
Reads a sentence, splits it into words, and shows the total
number of words, the first and last word, and the shortest
and longest words by length.

Inputs:
- sentence (string)

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validations:
- sentence must not be empty after strip().
- Must contain at least one word after split().

Test cases:
1) Normal: "the quick brown fox" -> count 4, first "the",
            last "fox", shortest "the", longest "quick"
2) Border: "hello" -> count 1, all words "hello"
3) Error:  "" -> "Error: invalid input"
"""

text = input("Enter a sentence:  ")
strip_text = text.strip()
list_words = strip_text.split()
word_count = len(list_words)

if strip_text == "":
    print("Error: invalid input")
else:
    first_word = list_words[0]
    last_word = list_words[-1]
    longest = max(list_words, key=len)
    shortest = min(list_words, key=len)

    print(f"Word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"Last word: {last_word}")
    print(f"Longest word: {longest}")
    print(f"Shortest word: {shortest}")

# Problem 5: Password strength classifier
"""
Description:
Reads a password and classifies it as "weak", "medium" or
"strong" based on length and character types (uppercase,
lowercase, digit, symbol).

Inputs:
- password_input (string)

Outputs:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validations:
- Password must not be empty.
- Length is checked with len().

Rules:
- weak:   length < 8, or only lowercase letters (very simple).
- strong: length >= 8 and contains at least one uppercase,
         one lowercase, one digit, and one symbol.
- medium: anything else (length >= 8 with some variety).

Test cases:
1) Normal: "Abc123!x" -> "Password strength: strong"
2) Border: "abcdefgh" -> "Password strength: weak"
3) Error:  ""         -> "Error: invalid input"
"""

password_input = input("Enter a password: ")

if password_input == "":
    print("Error: invalid input")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False

    for ch in password_input:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if not ch.isalnum():
            has_symbol = True

    if len(password_input) < 8 or (has_lower and not has_upper and not has_digit and not has_symbol):
        print("Password strength: weak")
    elif has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")

# Problem 6: Product label formatter (fixed-width text)
"""
Description:
Reads a product name and a price, builds a single-line
label in the format "Product: <NAME> | Price: $<PRICE>",
and adjusts it to exactly 30 characters (pads with spaces
if shorter, truncates if longer).

Inputs:
- product_name (string)
- price_value (string, must be numeric)

Outputs:
- 'Label: "<exactly 30 characters>"'

Validations:
- product_name must not be empty after strip().
- price_value must not be empty after strip().
- price_value must be a valid positive number.

Test cases:
1) Normal: "Laptop", "999.99" -> label padded/truncated to 30 chars
2) Border: "A", "1"          -> short label padded with spaces
3) Error:  "", "100"         -> "Error: invalid input"
"""

product_name=input("Enter product: ")
strip_product= product_name.strip()
price_name=input("Enter price: ")
string_price = str(price_name)
strip_price= string_price.strip()

if strip_product == "" or strip_price == "":
    print("Error: invalid input")
elif not strip_price.replace(".", "").isdigit():
    print("Error: invalid input")
else:
    label = f"Product: {strip_product} | Price: ${strip_price}"

    if len(label) > 30:
        label = label[:30]
    else:
        label = label + " " * (30 - len(label))

    print(f'Label: "{label}"')

# CONCLUSIONES
"""
   El manejo de strings es fundamental en la entrada y salida de
   datos, ya que casi toda la informacion que recibe un programa
   llega como texto. Metodos como lower(), strip(), split() y
   join() permiten normalizar y procesar ese texto de forma
   limpia y segura. Normalizar antes de comparar evita errores
   por mayusculas, espacios extra o formatos inconsistentes.
   Diseñar validaciones claras (primero vacio, luego formato)
   ayuda a evitar datos basura y hace el codigo mas robusto.
   Ademas, comprender la inmutabilidad de los strings y el uso
   de slices permite manipular texto sin efectos inesperados.
   En conjunto, estos 6 problemas refuerzan la importancia de
   validar, normalizar y transformar texto correctamente.
"""
# REFERENCES
"""
   1) Python documentation - Built-in Types: Text Sequence Type - str.
      https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
   2) Python documentation - String Methods.
      https://docs.python.org/3/library/stdtypes.html#string-methods
   3) Python documentation - Built-in Functions (len, min, max).
      https://docs.python.org/3/library/functions.html
   4) W3Schools - Python Strings.
      https://www.w3schools.com/python/python_strings.asp
   5) Real Python - Python String Methods.
      https://realpython.com/python-strings/
"""