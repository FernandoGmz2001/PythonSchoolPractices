# Crea un programa que lea del teclado el nombre de un archivo en formato .csv con la siguiente estructura 
#Nombre del producto, Precio, Cantidad minima a comprar, para que al menos con 20 lineas de entrada realice lo siguiente mediante una function
# Crear un segundo archivo con el nombre libre a eligir que sera llenado en base a lo siguiente 
# Nombre del producto, en caso de existir otro poducto con el mismo nombre se realizara lo siguiente
# Verificar si hay diferencias en el Precio o Cantidad minima a comprar de ser asi pedirle al usuario mediante consola 
    #eligir uno de los 2 valores a conservar y solo mostrar una linea del producto con los valores modificados

import csv
import os

def leer_csv(nombre_archivo):
    datos = []
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            datos = [fila for fila in lector]
    return datos

def escribir_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        fieldnames = datos[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(datos)

def procesar_archivo(entrada, salida):
    datos_entrada = leer_csv(entrada)
    datos_salida = []
    
    for fila in datos_entrada:
        nombre = fila['Nombre del producto']
        precio = float(fila['Precio'])
        cantidad_minima = int(fila['Cantidad minima a comprar'])
        
        # Verificar si ya existe un producto con el mismo nombre
        existe = False
        for producto in datos_salida:
            if producto['Nombre del producto'] == nombre:
                existe = True
                # Verificar si hay diferencias en Precio o Cantidad minima a comprar
                if producto['Precio'] != precio or producto['Cantidad minima a comprar'] != cantidad_minima:
                    print(f"Se encontró un producto duplicado: {nombre}")
                    print(f"Precio actual: {producto['Precio']}, Nuevo precio: {precio}")
                    print(f"Cantidad actual: {producto['Cantidad minima a comprar']}, Nueva cantidad: {cantidad_minima}")
                    opcion = input("Elija una opción (precio/nueva cantidad): ").strip().lower()
                    if opcion == 'precio':
                        producto['Precio'] = precio
                    elif opcion == 'cantidad':
                        producto['Cantidad minima a comprar'] = cantidad_minima
                break
        
        if not existe:
            datos_salida.append({'Nombre del producto': nombre, 'Precio': precio, 'Cantidad minima a comprar': cantidad_minima})
    
    escribir_csv(datos_salida, salida)
    print("Proceso completado. El archivo de salida ha sido generado.")

def main():
    archivo_entrada = input("Ingrese el nombre del archivo de entrada (.csv): ")
    archivo_salida = input("Ingrese el nombre del archivo de salida (.csv): ")
    
    procesar_archivo(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()
