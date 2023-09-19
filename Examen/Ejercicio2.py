#Se requiere hacer un programa que indique cual es mayor de dos numeros con 3 digitos cada uno pero hay un problema con la interfaz y este toma los numeros al reves.

#Entradas n1 = 734 n2 = 893 SALIDA : 437
#Entradas n1 = 221 n2 = 231

num1  = (input("Ingrese el primer numero: "))
num2 = (input("Ingrese el segundo numero: "))

num1 = num1[::-1]
num2 = num2[::-1]
num1 = int(num1)
num2 = int(num2)
if(num1> num2):
    print(num1)
elif(num1 == num2):
    print("Son iguales")
else:
    print(num2)