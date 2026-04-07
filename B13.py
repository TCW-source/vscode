#等差級數
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    m = int(LS[0])
    Max = int(LS[1])
    total = 1
    last_term = 0
    n = 1
    while True:
        next_term = n*m+1
        if total + next_term <= Max:
            total += next_term
            last_term = next_term
            n += 1
        else:
            break
    print(last_term)