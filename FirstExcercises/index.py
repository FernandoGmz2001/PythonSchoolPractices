def addProducts(*args):
    total = 0
    for arg in args:
        total += arg
    print('El resultado total es: ', total)


addProducts(5,5,5,5,5)

abcList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def deleteAbcPairs(abcList):
    newAbcList = []
    for index, letter in enumerate(abcList):
        if index % 2 != 0:
            newAbcList.append(letter)
    print(newAbcList)
deleteAbcPairs(abcList)
