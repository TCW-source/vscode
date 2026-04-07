#補數
N = eval(input())
for i in range(N):
    S = input()
    X = ''
    for s in S:
        if s == '0':
            X+='1'
        if s == '1':
            X+='0'
    Y = int(X,2)+1
    Z = f'{Y:b}'
    print(Z.zfill(len(S)))