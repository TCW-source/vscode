#完全平方數


import math
N = eval(input())
for i in range(N):
    S = input().split(' ')
    a = eval(S[0])
    b = eval(S[1])
    X = math.ceil(a**0.5)
    Y = math.floor(b**0.5)
    sum = 0
    for j in range(X,Y+1):
        sum+=(j*j)
    print(sum)