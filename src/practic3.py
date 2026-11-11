"""
   3. Vamos a realizar un programa que de nombre e info
"""
name=input("¿Como te llamas?\n")
age_txt=input("¿Cual es tu edad?\n")

#De esta forma en caso de que se introduzcan palabras, 
#no truena el codigo
try:
    age=int(age_txt)
    if age !=-1 and age >0:
        print(f"Hola {name.title()}, tu edad es {age}años")
        print(f"En Corea tendrias {age + 1}")
except:
    print("Solo edades enteras y en numeros enteros porfavor")
"""
#Esta seria una forma tradicional y directa de hacerlo
print(f"Hola {name.title()}, tu edad es {age_txt}años")
print(f"En Corea tendrias {int(age_txt) + 1}") 
"""
"""
   4. Practica, hacer un ticket donde ya calcules el precio, 
   la propina y el IVA
"""
subtotal_txt=input("Subtotal (MXN)\n")
IVA_txt=input("IVA (%) ejemplo 16\n")
tip=float(tip)

"""
   5. Calcular el peso, altura y masa corporal de una persona
"""
wight_txt=input("Peso en (kg): ")
heigt_txt=input("Altura en (m): ")

try:
   weight=float(wight_txt)
   heigt=float(heigt_txt)
   inc=weight/heigt(**2)
   print(f"Tu masa corporal es {inc}")
except ValueError:
   print("Datos no validos. EJ. peso: 70.5, altura 1.65")
except ZeroDivisionError:
   print("La altura debe ser diferente de 0")
except Exception:
   print(Exception)
except Exception as err:
   print(err)
print("Proceso posteriores")