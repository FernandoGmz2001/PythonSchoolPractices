# #4 Entrada de datos y estructuración.  
# Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture 
# las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato 
# “{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre y una LISTA de 
# todas las materias

dicc_reticula = dict([])

while True:
    asignatura = input("Digite la materia: ")
    creditos = int(input("Digite el numero de creditos de la materia: "))

    #add the vars to a dict
    dicc_reticula[asignatura] = creditos

    done = input("Desea continuar? (s/n)")
    if done == "n":
        break

for asignatura, creditos in dicc_reticula.items():
    print(f"{asignatura} tiene {creditos} creditos.")

materias = list(dicc_reticula.keys())
print(f"Las materias de este semestre son las siguientes: {asignatura}")

sum_creds = sum(dicc_reticula.values())
print(f"La suma de los creditos del semestre es de : {sum_creds}")












