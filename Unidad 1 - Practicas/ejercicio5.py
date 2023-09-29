# #5 Manejo de información  
# Escribir una función que reciba n parámetros de 
# llave valor e imprima la información en formato 
# “{valor}”: “{llave}”  

kwargs = dict([])

while True:
    k = input("Escriba la llave: ")
    v = input("Escriba el valor: ")

    #Add to the dict
    kwargs[k] = v
    
    done = input("Desea continuar? (s/n)")
    if done == "n":
        break

for key, value in kwargs.items():
        print(value," : ",key)
        
    