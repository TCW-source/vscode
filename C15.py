#迴文判定
N = eval(input())
for i in range(N):
    S = input()
    RS = S[::-1]
    if RS == S:
        print("Yes")
    else:
        print("No")