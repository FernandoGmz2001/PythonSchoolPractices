#Se requiere hacer un programa que indique cual es mayor de dos numeros con 3 digitos cada uno pero hay un problema con la interfaz y este toma los numeros al reves.

#Entradas n1 = 734 n2 = 893 SALIDA : 437
#Entradas n1 = 221 n2 = 231

# Entradas
num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

# Validación de longitud
if len(num1) != 3 or len(num2) != 3:
    print("Los números deben tener 3 dígitos cada uno.")
    exit()

# Validación de caracteres numéricos
if not num1.isdigit() or not num2.isdigit():
    print("Los números deben ser enteros.")
    exit()

# Invertir los números
num1 = int(num1[::-1])
num2 = int(num2[::-1])

# Comparar y mostrar resultado
if num1 > num2:
    print(num1)
elif num1 == num2:
    print("Los números son iguales.")
else:
    print(num2)