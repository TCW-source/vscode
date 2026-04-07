#計算阿拉伯數字出現次數
N = eval(input())
for i in range(N):
    S = input()
    LS = []
    for j in range(10):
        LS.append(0)
    for s in S:
        LS[int(s)] += 1
    RV = ''
    for ls in LS:
        RV += str(ls)
    print(RV)