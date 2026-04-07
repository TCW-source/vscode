#豹子
n = eval(input())
for i in range(n):
    S = input().split(' ')
    if S[0] == S[1] and S[0] == S[2]:
        print('Yes')
    else:
        print('No')

