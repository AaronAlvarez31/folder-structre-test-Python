# Numeros en Python
 # Numeros enteros

"""
Los numeros enteros lod podemos sumer( + ), 
restar( - ), multimplicar( * ) o dividir ( / )
"""

print(2+3) # suma
print(2-3) # resta
print(2*3) # multiplicacion
print(2/3) # division
print(2**3) # potencias
print(10%2) # modulo (mod)
print("")

print("Ejemplo de las operaciones")
print("2+3=",2+3)
print("2-3=",2-3)
print("2*3=",2*3)
print("2/3=",2/3)
print("2^3=",2**3)
print("20%2=",10%2)
print("")

number_1 = 5
number_2 = 10

print(number_1 + number_2 )
print("")


# Imprimir la edad de alguien
age = 34 # variable tipo int
# mensaje = "Charly tiene" + age + "años" (TypeError)

# método Build-in str()
message = "Charly tiene " + str(age) + " años"
print(message)

message_f =f"Charly tiene " + str{age} + " años"
print(message_f)

"""
TypeError: Python no puede reconocer el tipo de 
información 
"""

# métodos Build-in tyoe()
print(type(age), type("hola"), type(0.54), type(True))