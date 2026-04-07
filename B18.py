data = input().split(' ')
m = int(data[0])
n = int(data[1])

A = []
for i in range(m):
    a = input().split(' ')
    A.append(a)

for j in range(n):
    B = []
    for r in range(m):
        B.append(A[r][j])
    
    print(*B)