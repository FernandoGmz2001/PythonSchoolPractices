# En una matriz de 5x4 pedirle al usuario los valores.
# En una segunda matriz de 5x4, guardar un 1 si es el mismo numero guardado en la posicion anterior.
# Si es multiplo de 3 guardar un 2, si el numero es multiplo de 5 guardar un 3, y un 4 si es multiplo de 3 y 5
# a la vez. Si no se cumplen ninguna de las anteriores reglas guardar un 0.
matriz = [[],[],[],[]]
matriz2 = [[],[],[],[]]




i = 0
y = [1,2,3,4,5]
while i <= 3:
    print(f'Lista: {i+1}')
    for x in y:# while y <= 4:
        #print(f"i: {i}")
        #print(f"y: {y}")
            # print(f"Ingrese valor para posicion : {i}/20\n")
        curValue = int(input("Ingrese un valor numerico: "))
        matriz[i].append(curValue)
        
        # if x == 4:
        #     break
        # else:
        #     y+=1
        
    if i == 3:
        break
    else:
        i+= 1

    # print(matriz)


print(matriz)




