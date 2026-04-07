#間隔數
N = eval(input())
for i in range(N):
    S = input()
    Key1 = False
    Key2 = False

    if len(set(S)) == 2:
        Key1 = True

    if S[0] != S[1] and S[1] != S[2] and S[2] != S[3]:
        Key2 = True

    if Key1 and Key2:
        print('Yes')
    else:
        print('No')

        