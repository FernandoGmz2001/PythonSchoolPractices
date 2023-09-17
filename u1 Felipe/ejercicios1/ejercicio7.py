# #7 Formateo y conversiones  
# Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir 
# YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha 
# del día de hoy en el formato seleccionado. 

from datetime import date

today = date.today()

x = int(input('1.- Imprimir YYYY/MM/DD” la segunda “\n2.- Imprimir MM/DD/YYYY”\n'))
match x:
    case 1:
        d1 = today.strftime("%Y/%m/%d")
        print(d1)
    case 2:
        d2 = today.strftime("%m/%d/%Y")
        print(d2)
    case _:
        print("Error")
