def addProducts(*args):
    total = 0
    for arg in args:
        total += arg
    print('El resultado total es: ', total)


addProducts(5,5,5,5,5)