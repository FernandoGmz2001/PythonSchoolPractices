#Crear una funcion que reciba como parametro una palabra, dicha funcion leera un archivo.txt, el cual debe tener un texto a elegir de su preferencia (poner la referencia) de al menos 200 palabras o mas, la funcion debe devolver la cantidad de veces que se repite la palabra y sus posiciones tomando en cuenta el primer caracter.
import sys
print(sys.stdout.encoding)

import re

def contar_palabras():
    insertedWord = input('Ingrese la palabra a buscar: ')
    archivo = open("ArchivoTexto.txt")
    texto = archivo.read()
    texto = texto.rstrip()
    print(texto)
    
    # Utilizar una expresión regular para dividir el texto en palabras
    separatedWords = re.findall(r'\b\w+\b', texto.lower())
    
    contadorPalabrasRepetidas = 0
    print(separatedWords)
    positionList = []
    for (index, word) in enumerate(separatedWords):
        if word == insertedWord.lower():
            positionList.append(index)
            contadorPalabrasRepetidas += 1
    
    if contadorPalabrasRepetidas == 0:
        print('La palabra no se encontró en el texto.')
    else:
        print('Las posiciones donde se encuentra la palabra son: ', positionList)
        print('La palabra se repite ', contadorPalabrasRepetidas, ' veces')

contar_palabras()
