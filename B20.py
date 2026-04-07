#分數加法
K = int(input())

for _ in range(K):
    fractions = input().split() # 得到像是 ['1/2', '1/6', '3/2']
    
    # 步驟 1：處理第一個分數
    parts = fractions[0].split('/')
    res_a = int(parts[0]) # 總和的分子
    res_b = int(parts[1]) # 總和的分母
    
    # 步驟 2：從第二個分數開始往後加
    for i in range(1, len(fractions)):
        next_parts = fractions[i].split('/')
        next_a = int(next_parts[0])
        next_b = int(next_parts[1])
        
        # 分數加法公式： (a/b) + (c/d) = (ad + bc) / (bd)
        # 這裡 res_a/res_b 是「目前的總和」
        # 這裡 next_a/next_b 是「新加入的分數」
        res_a = res_a * next_b + next_a * res_b
        res_b = res_b * next_b
        
        # 步驟 3：加完一筆就立刻約分 (GCD)，防止數字噴太大
        # 我們找 res_a 和 res_b 的最大公因數
        a, b = res_a, res_b
        while b:
            a, b = b, a % b
        gcd_val = a # 這就是最大公因數
        
        res_a //= gcd_val
        res_b //= gcd_val
        
    # 輸出結果
    print(str(res_a) + "/" + str(res_b))