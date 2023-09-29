n = int(input("Digite un numero: "))
lb = []
l1 = []
if n >= 2 and n <= 10:
    i = 0
    u = 1
    for x in range(n):
        while i < n:
            l1.append(u)
            i += 1
            u += 1
        i = 0
    print(l1)

arr = [[0 for i in range(n)] for j in range(n)] 
 
level = 0 
pos = 0 
 
while pos < n * n: 
    num = n - (level * 2) - 1 
    temPos = pos 
 
    for i in range(num): 
        temPos += 1 
        arr[level][i+level] = temPos 
        arr[level+i][n-level-1] = temPos + num 
        arr[n-level-1][n-level-i-1] = temPos + num * 2 
        arr[n-level-i-1][level] = temPos + num * 3 
        if num == 2: 
            arr[n-level-i-1][level+1] = temPos + num * 3 + 1 
            pos += 1 
 
    level += 1 
    pos += num * 4 
 

for i in arr: 
    for j in i: 
        print('%3s' % j, end='') 
    print("")