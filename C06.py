#愛找麻煩的老師
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    iLS = []
    for ls in LS:
        iLS.append(eval(ls))
    aLS = iLS[::]
    aLS.sort()
    if iLS == aLS:
        print('YES')
    else:
        print('NO')
