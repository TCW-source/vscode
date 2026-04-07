#豬式拉丁語
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    result = []
    for ls in LS:
        NLS = ls[1:]+ls[0]
        NLS+='ay'
        result.append(NLS.upper())
    print(*result)