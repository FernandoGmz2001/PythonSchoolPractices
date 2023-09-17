#escribir programa que pregunte el nombre de un producto, su precio y numero de unidades
#y mostrar en pantalla una cadena con el nombre del producto, seguido del precio
#unitario seguido de 6 digitos enteros y 2 decimales.
#el numero de unidades con 3 digitos y el coste total con 8 digitos enteros y 2 decimales


nombre = input("Ingrese el nombre: ") 
precio_u= float(input ("ingrese el precio unitario:"))
unidades = int (input('ingrese la cantidad:' ))   

precio_uni = str(precio_u)
costototal=(precio_u*unidades) 

print ('El nombre del producto es: ', nombre,'\n','\nSu precio unitario es ',"%09.2f" % precio_u,
        'pesos \n','\nLa cantidad de unidades compradas fue: ', "%03.0f" % (unidades),'unidades.',
        '\n','\n El costo total es: ',("%011.2f" % (costototal)))

