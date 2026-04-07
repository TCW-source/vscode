#魔術抽號順序
N = eval(input())
for i in range(N):
    S = input().split(' ')
    Max = -1
    Min = -1
    RV = 'YES'
    for s in S:
        NowV = int(s)
        if Max == -1:
            Max = NowV
            Min = NowV
        else:
            if NowV < Max and NowV > Min:
                RV = 'NO'
                break
            elif NowV > Max:
                Max = NowV
            elif NowV < Min:
                Min = NowV
    print(RV)