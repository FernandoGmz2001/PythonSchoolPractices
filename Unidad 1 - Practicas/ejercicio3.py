def reverseName():
    name = input('Ingrese su nombre: ')
    reversedName = ''.join(reversed(name))
    newName = ''
    for index,letter in enumerate(reversedName):
        if index % 2 == 0:
            newName += letter.upper()
        else:
            newName += letter
    print(newName)

reverseName()