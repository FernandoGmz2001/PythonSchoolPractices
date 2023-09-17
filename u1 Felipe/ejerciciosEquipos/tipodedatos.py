# una jugueteria tiene mucho exito en dos de sus productos.
# Payasos y muñecas. Se suele hacer la venta por correo y la
# empresa de logistica les cobra por peso de cada paquete.
# Calcular el peso de los payasos y muñecas. Cada payaso pesa
# 112g y cada muñeca 75g.
#Calcular el peso total del paquete y calcular el precio total
#si por cada 100g de payaso se cobra $3 y por cada 100g de muñeca
#cobra $2

payasos = int(input("Digite el numero de payasos:\n"))
dolls = int(input("Digite el numero de muñecas:\n"))

peso_payasos = float((payasos * 112))#g
peso_dolls = float((dolls * 75))#g

costo_payasos = float((peso_payasos*3)/100)
costo_dolls = float((peso_dolls*2)/100)

print(f"El peso total del paquete es de: {(peso_payasos/1000)+(peso_dolls/1000)} kg.\nEl costo total es de: ${costo_payasos+costo_dolls}") 








