#判斷長字串
N = eval(input())
for i in range(N):
    LS = input().split()
    Ct=0
    for ls in LS:
        if len(ls) >= 10:
            Ct+=1
    print(Ct)