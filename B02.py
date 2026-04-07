#add digits
N = eval(input())
for i in range(N):
    S=input()
    while len(S)>1:
        total=0
        for s in S:
            total+=int(s)
        S = str(total)
    print(S)