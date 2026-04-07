#計算candy
N = eval(input())
for i in range(N):
    S = int(input())
    C = S
    P = S
    while P >= 3:
        CT = P//3
        P -= 3*CT
        C += CT
        P += CT
    print(C)