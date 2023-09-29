# Escribir un programa en consola que permita capturar cadenas de texto hasta que el usuario
# lo desee. Con una funcion mostrar en pantalla una cadena con todas las palabras utilizadas en las
# cadenas capturadas en orden alfabetico, los numeros se mostraran hasta el final de la cadena.

cadenas = []

done = False
while not done:
    frase = input("Escriba una frase: \n")
    cadenas.append(frase)

    i = 0
    while i == 0:
        x = input("Quiere escribir otra frase? (s/n)")
        if x == "s":
            
            i = 1
            break
        if x== "n":
            i = 1
            done = True
            break
        else:
            print("Ups. No entendi eso!")
    
inputString = ""
for c in range(len(cadenas)):
    inputString += str(cadenas[c]) + " "

palabras = []
numeros = []

for palabra in inputString.split():
    if palabra.isnumeric():
        numeros.append(palabra)
    else:
        palabras.append(palabra)

# Ordenar las listas por separado
palabras.sort()
numeros.sort()

# Concatenar las listas para obtener la salida final
palabras.extend(numeros)

# Imprimir el resultado
print("Palabras ordenadas:")
print(" ".join(palabras))
