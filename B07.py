#Armstrong Number
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    n = int(LS[0])
    m = int(LS[1])
    result = []
    for num in range(n,m+1):
        s_num = str(num)
        k = len(s_num)
        total = 0
        for char in s_num:
            digit = int(char)
            total += int(char)**k
        if total == num:
            result.append(num)
    if len(result) == 0:
        print('none')
    else:
        print(*result)