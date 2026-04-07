#反轉字串
N = eval(input())
for i in range(N):
    S = input()
    #例如，如果 S 是 "abc"，則 RS 是 "cba"
    RS = S[::-1]
    #初始化空字串
    RV = ''
    for rs in RS:
        if RV == '':
            RV = rs
        else:
            RV += f',{rs}'
    print(RV)