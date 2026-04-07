#因數分解
N = eval(input())
for i in range(N):
    num = int(input())
    X=2
    result=[]
    while num>1:
        if num % X == 0:
            result.append(X)
            num = num / X
        else:
            X+=1
    print(*result)