# una pizzeria ofrece pizzas vegetarianas o no vegetarianas y aparece una lista de ingredientes
# vegetarianos y no vegetarianos
# los ingredientes vegetarianos son: pimiento y tofu
# ingredientes no vegetarianos son: pepperoni jamon y salami

# escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
# en funcion de su respuesta mostrar el menu con los ingredientes. 

# Solo se puede elegir un ingrediente ademas de la mozzarella y el tomate que estan en todas las pizzas.
# Al final mostrar una lista con los ingredientes de la pizza y el tipo de la pizza

vegetariana =(input("Quiere una pizza vegetariana? (s/n)"))

ingrediente = str()

if vegetariana == "s":

            while True:
                i = int(input("Escoja un ingrediente:\n 1. Pimiento\n2. Tofu\n"))

                if i == 1:
                    ingrediente = "Pimiento"
                    break
                if i == 2:
                    ingrediente = "Tofu"
                    break
                

                print(f"Su pizza contiene los siguientes ingredientes:\nMozzarella\nTomate\n{ingrediente}\n\nSu tipo de pizza es: vegetariana")

if vegetariana == "n":

    while True:
        i = int(input("Escoja un ingrediente:\n 1. Pepperoni\n2. Jamon\n3.Salami\n"))

        if i == 1:
            ingrediente = "Pepperoni"
            break
        if i == 2:
            ingrediente = "Jamon"
            break
        if i == 3:
            ingrediente = "Salami"
            break

    print(f"Su pizza contiene los siguientes ingredientes:\nMozzarella\nTomate\n{ingrediente}\n\nSu tipo de pizza es: no vegetariana")






