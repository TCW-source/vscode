#翻轉吧字串
N = eval(input())
for i in range(N):
    S = input().split(' ')
    A = int(S[0])
    B = S[1]
    width = len(B)//A
    RV=''
    for j in range(0, len(B), width):
        C = B[j:j+width]
        RV+=C[::-1]
    print(RV)


