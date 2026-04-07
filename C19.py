#負2為底數字轉換
def to_negabinary(n):
    if n == 0: return 0
    res = ""
    while n != 0:
        remainder = n % -2
        n //= -2
        if remainder < 0:
            remainder += 2
            n += 1
        res = str(remainder) + res
    return res

count = int(input())
for i in range(1, count + 1):
    n = int(input())
    print(to_negabinary(n))