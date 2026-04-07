#國際標準書號
N = eval(input())
for i in range(N):
    LS = input()
    dig = ''
    for ls in LS:
        if ls != '-':
            dig += ls
    S = 0
    for k in range(len(dig)):
        num = int(dig[k])
        if (k+1)%2 == 1:
            S += num*1
        else :
            S += num*3
    M = S % 10
    N = 10 - M
    if N == 10:
        print(f'ISBN {LS}-0')
    else:
        print(f'ISBN {LS}-{N}')