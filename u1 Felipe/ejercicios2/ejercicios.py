# dividir un cierto entero n por otro entero n hasta n-1
# obteniendo una secuencia de numeros, cada numero de esa secuencia almacenado en una lista
# la secuencia se deben cumplir hasta llegar a n-1

# si n=1 imprimir la secuencia entera
# si no, imprimir secuencia invalida

n = int(input("Digite un entero: "))
m = int(input("Digite el numero divisor: "))

list = []
i = 0
while n >= 1:
    ni = int()
    if n % m  == 0:
        ni = int(n)
    if ni != 0:
        list.append(ni)
    else:
        list.append(n)
    
    if n > 1:
        if n % m >= 1:
            print("Secuencia invalida")
            break

    n = n / m

    if n==1:
        ni = int(n)
        list.append(ni)
        print(list)
if n or m == 0:
    print("Secuencia invalida")
if n or m < 0:
    print("Secuencia invalida")







