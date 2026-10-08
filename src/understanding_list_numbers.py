# Metodod nuild-in range
"""
El metodo 'range()' nos ayuda a crear una 
serie de numeros facilmente.
"""

for value in range(1,10):
    print(value)

# Lista de numeros (list y range)
numbers=list(range(0,10))
print(numbers)

# Lista de numeros pares (list y range)
even_numbers=list(range(0,11,2))
print(even_numbers)

# Lista de numeros impares (list y range)
impar_numbers=list(range(1,11,2))
print(impar_numbers)

# Lista de numeros pares (list y range)
cinco=list(range(5,5,5))
print(cinco)

# Crear una lista con los primeros diez numeros cuadraticos
squares=[]
for value in range(1,11):
    square=value**2
    print(f"el numero que calcule es {square}")
    squares.append(square)
print(squares)