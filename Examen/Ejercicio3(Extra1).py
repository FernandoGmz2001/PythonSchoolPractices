# Realice un programa que use las 2 siguientes clases

# Locacion:
# Nombre(Nombre de la locacion)
# Porcentaje de IVA(un valor flotante)
# Items(Lista de items)

# Item:
# Nombre(Nombre del Item)
# Cantidad(Cantidad entera)
# Precio(numero flotante calculado multiplicando el valor * el IVA de la locacion)

# Realizar un programa en el cual me permita capturar items por locacion y mediante una funcion en la locacion me permita obtener el total de capital que tiene dicha locacion(sumatoria de los items)

# En dado caso agregar un item existene a una locacion mostrar mensaje de item ya existente.
# La informacion tiene que ser capturada por el usuario

class Item:
    def __init__(self, nombre, cantidad, valor, porcentaje_iva):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = valor * (1 + porcentaje_iva)  # Se calcula el precio incluyendo el IVA

class Locacion:
    def __init__(self, nombre, porcentaje_iva):
        self.nombre = nombre
        self.porcentaje_iva = porcentaje_iva
        self.items = []

    def agregar_item(self, nombre, cantidad, valor):
        for item in self.items:
            if item.nombre == nombre:
                print(f"El item '{nombre}' ya existe en la locación.")
                return
        nuevo_item = Item(nombre, cantidad, valor, self.porcentaje_iva)
        self.items.append(nuevo_item)
        print(f"Item '{nombre}' agregado a la locación '{self.nombre}'.")

    def calcular_total(self):
        total = sum(item.precio * item.cantidad for item in self.items)  # Se calcula el total multiplicando precio por cantidad
        return total

def main():
    locaciones = []
    
    while True:
        print("\n1. Crear Locación")
        print("2. Agregar Item a Locación")
        print("3. Calcular Total de Locación")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre de la locación: ")
            porcentaje_iva = float(input("Ingrese el porcentaje de IVA (por ejemplo, 0.16 para 16%): "))
            locacion = Locacion(nombre, porcentaje_iva)
            locaciones.append(locacion)
            print(f"Locación '{nombre}' creada.")
        
        elif opcion == "2":
            if not locaciones:
                print("Primero debe crear una locación.")
                continue
            print("\nLocaciones existentes:")
            for i, locacion in enumerate(locaciones, start=1):
                print(f"{i}. {locacion.nombre}")
            
            locacion_index = int(input("Seleccione una locación (por número): ")) - 1
            if locacion_index < 0 or locacion_index >= len(locaciones):
                print("Selección de locación inválida.")
                continue
            
            locacion = locaciones[locacion_index]
            nombre = input("Ingrese el nombre del item: ")
            cantidad = int(input("Ingrese la cantidad: "))
            valor = float(input("Ingrese el valor unitario: "))
            locacion.agregar_item(nombre, cantidad, valor)
        
        elif opcion == "3":
            if not locaciones:
                print("Primero debe crear una locación.")
                continue
            print("\nLocaciones existentes:")
            for i, locacion in enumerate(locaciones, start=1):
                print(f"{i}. {locacion.nombre}")
            
            locacion_index = int(input("Seleccione una locación (por número): ")) - 1
            if locacion_index < 0 or locacion_index >= len(locaciones):
                print("Selección de locación inválida.")
                continue
            
            locacion = locaciones[locacion_index]
            total = locacion.calcular_total()
            print(f"Total de capital en '{locacion.nombre}': ${total:.2f}")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
