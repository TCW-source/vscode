#進制轉換
def dec_to_base4(n):
    if n == 0: return "0"
    res = ""
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    return res

# 讀取筆數 X
x = int(input())

for _ in range(x):
    octal_str = input()
    # 先將 8 進制字串轉成 10 進制整數
    decimal_num = int(octal_str, 8)
    # 再轉成 4 進制字串並輸出
    print(dec_to_base4(decimal_num))