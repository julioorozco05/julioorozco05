# Función de suma:
def suma(num1: int, num2: int):
    return num1 + num2

print(suma(num1 = 5, num2 = 10))

# Función de resta:
def resta(num1: int, num2: int):
    return num1 - num2

print(resta(num1 = 20, num2 = 10))

# funcion de division:
def division(num1: int, num2: int):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error, no se puede dividir entre cero"

print(division(num1 = 10, num2 = 2))