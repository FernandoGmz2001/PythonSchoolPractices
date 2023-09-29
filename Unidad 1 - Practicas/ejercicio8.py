# 8.1.-Definir una clase usuario que contenga como atributos: 
# Usuario
# Contraseña
# Rol
# Nombre
# CURP
# Ciudad
# 8.2.-Realizar un programa que contenga el siguiente menú 
# 1.- Registro
# 2.- Inicio de sesión
# 3.- Salida 
# La opción de registro solicitara al usuario registrarse solicitando la información de los atributos la clase exceptuando el atributo Rol que por defecto será rol cliente, no se permitirán usuarios con CURP repetido en caso de mostrar mensaje de “El usuario ya existe” 
# La opción de inicio de sesión permitirá al usuario introducir sus credenciales al ser correctas desplegar en pantalla la información del usuario de lo contrario mostrar mensaje de “datos incorrectos“ 
# 8.3.- Declarar un usuario con rol “Administrador” el cual al momento de iniciar sesión despliegue la información de todos los usuarios registrados al momento.

class Usuario:
    def __init__(self, usuario, contraseña, nombre, curp, ciudad, rol="cliente"):
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad
        self.rol = rol

usuarios_registrados = []

def registrar_usuario():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    nombre = input("Ingrese su nombre: ")
    curp = input("Ingrese su CURP: ")
    ciudad = input("Ingrese su ciudad: ")
    
    # Verificar si el usuario ya existe
    for u in usuarios_registrados:
        if u.curp == curp:
            print("El usuario ya existe.")
            return
    
    nuevo_usuario = Usuario(usuario, contraseña, nombre, curp, ciudad)
    usuarios_registrados.append(nuevo_usuario)
    print("Usuario registrado con éxito.")

def iniciar_sesion():
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    
    for u in usuarios_registrados:
        if u.usuario == usuario and u.contraseña == contraseña:
            print(f"Información del usuario: \nUsuario: {u.usuario}\nNombre: {u.nombre}\nCURP: {u.curp}\nCiudad: {u.ciudad}\nRol: {u.rol}")
            return
    
    print("Datos incorrectos.")

# Usuario administrador
admin = Usuario("admin", "admin123", "Admin", "ADMIN123456789", "Nuevo Laredo", "Administrador")
usuarios_registrados.append(admin)

while True:
    print("Menú:")
    print("1.- Registro")
    print("2.- Inicio de sesión")
    print("3.- Salida")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
