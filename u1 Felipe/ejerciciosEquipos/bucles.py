#Bucles - escribir un programa en el que se pregunte una frase y una letra  y se muestre
#un mensaje que muestre el numero de veces que aparece la letra en la frase

phrase = str(input("Digite una frase: \n")).lower()
letter = str(input("Digite una letra:\n"))
print(f"La letra '{letter}' se repite: "+str(phrase.lower().count(letter)))
# count = 0

# for x in phrase:
#   if x == letter:
#     count= count+1
  
# print(f"Numero de veces que la letra '{letter}' aparece: {count}")




