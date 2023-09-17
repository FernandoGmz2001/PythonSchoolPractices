l1=[1,2,3,4,5,6,7,8,9,10]
l2=[11,12,13,14,15,16,17,18,19,20]
l3=[21,22,23,24,25,26,27,28,29,30]
l4=[31,32,33,34,35,36,37,38,39,40]
l5=[41,42,43,44,45,46,47,48,49,50]
l6=[51,52,53,54,55,56,57,58,59,60]
l7=[61,62,63,64,65,66,67,68,69,70]
l8=[71,72,73,74,75,76,77,78,79,80]
l9=[81,82,83,84,85,86,87,88,89,90]
l10=[91,92,93,94,95,96,97,98,99,100]
array = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10]
x = int(input("Digite una posicion: "))
sum = int()
i = int(0)
u = int(9)
if x >= 0 and x <= 9:
    for a in array:
        sum += a[x]
        print(sum)
elif x == 10:
    for a in array:
        sum += a[i]
        i += 1
    for b in array:
        sum += b[u]
        u -= 1
        
        print(sum)
elif x < 0 :
    print("No se aceptan numeros negativos.")

