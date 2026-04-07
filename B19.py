#辨識數字
N =eval(input())
for i in range(N):
    S =input()
    lenth = len(S)
    if lenth == 3:
        dif_one = 0
        target = 'one'
        for j in range(3):
            if S[j] != target[j]:
                dif_one+=1
        if dif_one<=1:
            print(1)
        else:
            print(2)

    elif lenth == 5:
        dif_three = 0
        target = 'three'
        for j in range(5):
            if S[j] != target[j]:
                dif_three+=1
        if dif_three<=1:
            print(3)
        else:
            print(8)