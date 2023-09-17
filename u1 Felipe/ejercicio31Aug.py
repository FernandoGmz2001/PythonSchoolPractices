
#escribir un programa que reciba un str de char y devuelva un
#diccionario con cada palabra que contenga y su secuencia
#


phrase = str(input("Digite una oracion: \n"))
count = {}

texto = phrase.split()
for s in texto:
  if s in count:
    count[s] += 1
  else:
    count[s] = 1

for key in count:
  print(key, count[key])

