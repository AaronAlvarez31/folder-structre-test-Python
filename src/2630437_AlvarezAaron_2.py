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
   En Python, int es un numero entero (sin decimales) y float es
   un numero con decimales. Un booleano (True/False) se obtiene
   a partir de comparaciones (por ejemplo, temp_c >= 30.0) y sirve
   para tomar decisiones con if. Validar rangos (horas >= 0,
   salario > 0) y evitar divisiones entre cero es importante para
   que el programa no falle. Este documento presenta 6 problemas
   resueltos con enteros, flotantes y booleanos, cada uno con
   descripcion, entradas, salidas, validaciones, casos de prueba
   y su codigo.
"""
# PRINCIPIOS Y BUENAS PRACTICAS
"""
   - Usar int para contadores y float para cantidades con decimales.
   - Evitar duplicar expresiones complejas: guardar resultados
     intermedios en variables.
   - Validar datos antes de operar (horas, salarios, etc.).
   - Usar nombres descriptivos y mensajes claros para el usuario.
   - Documentar que significa true y false en cada contexto.
"""

# Problem 1: Temperature converter and range flag
"""
Description:
   Converts a temperature in Celsius to Fahrenheit and Kelvin,
   and tells if it is a high temperature (>= 30.0 C).

Inputs:
   - temp_c (float)

Outputs:
   - "Fahrenheit: <temp_f>"
   - "Kelvin: <temp_k>"
   - "High temperature: true|false"

Validations:
   - temp_c must be convertible to float.
   - Kelvin must not be negative (temp_c >= -273.15).

Test cases:
   1) Normal: 25.0    -> F 77.0, K 298.15, high False
   2) Border: 30.0    -> F 86.0, K 303.15, high True
   3) Error:  -300.0  -> "Error: invalid input"
"""

try:
    temp_c = float(input("Temperature in Celsius: "))

    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15

    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        is_high_temperature = (temp_c >= 30.0)

        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {is_high_temperature}")

except ValueError:
    print("Error: invalid input")

# Problem 2: Work hours and overtime payment
"""
Description:
   Calculates weekly pay. Up to 40 hours are paid at hourly_rate.
   Extra hours (> 40) are paid at 150% of the rate.

Inputs:
   - hours_worked (float)
   - hourly_rate (float)

Outputs:
   - "Regular pay: <regular_pay>"
   - "Overtime pay: <overtime_pay>"
   - "Total pay: <total_pay>"
   - "Has overtime: true|false"

Validations:
   - hours_worked >= 0
   - hourly_rate > 0

Test cases:
   1) Normal: 45, 100  -> regular 4000, overtime 750, total 4750
   2) Border: 40, 100  -> regular 4000, overtime 0, total 4000
   3) Error:  -1, 100  -> "Error: invalid input"
"""

try:
    hours_worked = float(input("Hours worked: "))
    hourly_rate = float(input("Hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        if hours_worked > 40:
            regular_hours = 40
            overtime_hours = hours_worked - 40
        else:
            regular_hours = hours_worked
            overtime_hours = 0

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40)

        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")

except ValueError:
    print("Error: invalid input")

# Problem 3: Discount eligibility with booleans
"""
Description:
   Determines if a customer gets a 10% discount based on:
   is_student OR is_senior OR purchase_total >= 1000.0.

Inputs:
   - purchase_total (float)
   - is_student_text (string "YES" or "NO")
   - is_senior_text (string "YES" or "NO")

Outputs:
   - "Discount eligible: true|false"
   - "Final total: <final_total>"

Validations:
   - purchase_total >= 0.0
   - is_student_text and is_senior_text must be "YES" or "NO"

Test cases:
   1) Normal: 500.0, "YES", "NO"   -> eligible True, final 450.0
   2) Border: 1000.0, "NO", "NO"   -> eligible True, final 900.0
   3) Error:  -10.0, "YES", "NO"   -> "Error: invalid input"
"""

try:
    purchase_total = float(input("Purchase total: "))
    is_student_text = input("Is student (YES/NO): ").strip().upper()
    is_senior_text = input("Is senior (YES/NO): ").strip().upper()

    if purchase_total < 0.0:
        print("Error: invalid input")
    elif is_student_text != "YES" and is_student_text != "NO":
        print("Error: invalid input")
    elif is_senior_text != "YES" and is_senior_text != "NO":
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

        if discount_eligible:
            final_total = purchase_total * 0.9
        else:
            final_total = purchase_total

        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total}")

except ValueError:
    print("Error: invalid input")

# Problem 4: Basic statistics of three integers
"""
Description:
   Reads three integers and calculates sum, average, max, min,
   and whether all three are even.

Inputs:
   - n1, n2, n3 (int)

Outputs:
   - "Sum: <sum_value>"
   - "Average: <average_value>"
   - "Max: <max_value>"
   - "Min: <min_value>"
   - "All even: true|false"

Validations:
   - All three inputs must be convertible to int.

Test cases:
   1) Normal: 2, 4, 6   -> sum 12, avg 4.0, max 6, min 2, all even True
   2) Border: 1, 2, 3   -> sum 6, avg 2.0, max 3, min 1, all even False
   3) Error:  "a", 2, 3 -> "Error: invalid input"
"""

try:
    n1 = int(input("Number 1: "))
    n2 = int(input("Number 2: "))
    n3 = int(input("Number 3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"Sum: {sum_value}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")

except ValueError:
    print("Error: invalid input")

# Problem 5: Loan eligibility (income and debt ratio)
"""
Description:
   Determines if a person is eligible for a loan based on income,
   debt ratio, and credit score.

Inputs:
   - monthly_income (float)
   - monthly_debt (float)
   - credit_score (int)

Outputs:
   - "Debt ratio: <debt_ratio>"
   - "Eligible: true|false"

Validations:
   - monthly_income > 0.0
   - monthly_debt >= 0.0
   - credit_score >= 0

Test cases:
   1) Normal: 10000, 2000, 700  -> ratio 0.2, eligible True
   2) Border: 8000, 3200, 650   -> ratio 0.4, eligible True
   3) Error:  0, 100, 700       -> "Error: invalid input"
"""

try:
    monthly_income = float(input("Monthly income: "))
    monthly_debt = float(input("Monthly debt: "))
    credit_score = int(input("Credit score: "))

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")

except ValueError:
    print("Error: invalid input")

# Problem 6: Body Mass Index (BMI) and category flag
"""
Description:
   Calculates BMI from weight and height, and tells if the
   person is underweight, normal, or overweight.

Inputs:
   - weight_kg (float)
   - height_m (float)

Outputs:
   - "BMI: <bmi_rounded>"
   - "Underweight: true|false"
   - "Normal: true|false"
   - "Overweight: true|false"

Validations:
   - weight_kg > 0.0
   - height_m > 0.0

Test cases:
   1) Normal: 70, 1.75  -> BMI 22.86, normal True
   2) Border: 50, 1.80  -> BMI 15.43, underweight True
   3) Error:  0, 1.75   -> "Error: invalid input"
"""

try:
    weight_kg = float(input("Weight (kg): "))
    height_m = float(input("Height (m): "))

    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print(f"BMI: {bmi_rounded}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")

except ValueError:
    print("Error: invalid input")

# CONCLUSIONES
"""
   Los enteros y flotantes se usan juntos en calculos reales:
   int para contadores y edades, float para temperaturas, salarios
   o BMI. Las comparaciones generan booleanos que permiten tomar
   decisiones con if, y combinar condiciones con and, or y not
   permite modelar reglas como elegibilidad de prestamos o
   descuentos. Validar rangos y evitar divisiones entre cero es
   clave para que el programa no falle. Estos patrones se repiten
   en problemas de nomina, descuentos, prestamos y salud.
"""
# REFERENCES
"""
   1) Python documentation - Built-in Types: Numeric Types.
      https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
   2) Python documentation - Boolean Type.
      https://docs.python.org/3/library/stdtypes.html#boolean-type-bool
   3) Python documentation - Built-in Functions (round, abs, min, max).
      https://docs.python.org/3/library/functions.html
   4) W3Schools - Python Numbers.
      https://www.w3schools.com/python/python_numbers.asp
   5) Real Python - Python Numbers and Booleans.
      https://realpython.com/python-numbers/
"""