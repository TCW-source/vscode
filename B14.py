#小一算術分析器
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    n = int(LS[0])
    m = int(LS[1])
    carry = 0       # 參數 carry：記錄當前位數是否有進位 (0 或 1)
    carry_count = 0 # 參數 carry_count：總進位次數
    while n>0 or m>0:
        digit_n = n%10
        digit_m = m%10
        sum = digit_n + digit_m + carry
        if sum >= 10 :
            carry = 1
            carry_count += 1
        else:
            carry = 0
        n = n // 10
        m = m // 10
    print(carry_count)