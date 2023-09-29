# Crea un programa que lea del teclado el nombre de un archivo en formato .csv con la siguiente estructura 
#Nombre del producto, Precio, Cantidad minima a comprar, para que al menos con 20 lineas de entrada realice lo siguiente mediante una function
# Crear un segundo archivo con el nombre libre a eligir que sera llenado en base a lo siguiente 
# Nombre del producto, en caso de existir otro poducto con el mismo nombre se realizara lo siguiente
# Verificar si hay diferencias en el Precio o Cantidad minima a comprar de ser asi pedirle al usuario mediante consola 
    #eligir uno de los 2 valores a conservar y solo mostrar una linea del producto con los valores modificados

import csv
import os

def obtener_ruta(nombre_archivo):
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(directorio_actual, nombre_archivo)

def leer_csv(nombre_archivo):
    datos = []
    ruta_archivo = obtener_ruta(nombre_archivo)
    try:
        with open(ruta_archivo, newline='') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
    except FileNotFoundError:
        print("El archivo de entrada no se encuentra.")
    return datos

def escribir_csv(datos, nombre_archivo):
    ruta_archivo = obtener_ruta(nombre_archivo)
    with open(ruta_archivo, 'w', newline='') as archivo:
        fieldnames = datos[0].keys()
        escritor = csv.DictWriter(archivo, fieldnames=fieldnames)
        escritor.writeheader()
        escritor.writerows(datos)

def procesar_archivo(entrada, salida):
    datos_entrada = leer_csv(entrada)
    if datos_entrada:
        datos_salida = []
        for fila in datos_entrada:
            nombre = fila["Nombre del producto"]
            precio = fila["Precio"]
            cantidad = fila["Cantidad minima a comprar"]
            
            # Verificar si ya existe un producto con el mismo nombre
            existe = False
            for producto in datos_salida:
                if producto["Nombre del producto"] == nombre:
                    existe = True
                    # Comprobar si hay diferencias en precio o cantidad
                    if producto["Precio"] != precio:
                        print(f"El producto '{nombre}' tiene precios diferentes.")
                        usuario_elige = input("¿Cuál precio desea conservar (Nuevo/Antiguo)? ").strip().lower()
                        if usuario_elige == "nuevo":
                            producto["Precio"] = precio
                    if producto["Cantidad minima a comprar"] != cantidad:
                        print(f"El producto '{nombre}' tiene cantidades diferentes.")
                        usuario_elige = input("¿Cuál cantidad desea conservar (Nuevo/Antiguo)? ").strip().lower()
                        if usuario_elige == "nuevo":
                            producto["Cantidad minima a comprar"] = cantidad
            if not existe:
                datos_salida.append({"Nombre del producto": nombre, "Precio": precio, "Cantidad minima a comprar": cantidad})
        
        escribir_csv(datos_salida, salida)
        print("Archivo de salida creado con éxito.")
    else:
        print("No se pudieron procesar los datos de entrada.")

def main():
    archivo_entrada = input("Ingrese el nombre del archivo de entrada (en formato CSV): ")
    archivo_salida = input("Ingrese el nombre del archivo de salida (en formato CSV): ")
    procesar_archivo(archivo_entrada, archivo_salida)

if __name__ == "__main__":
    main()
