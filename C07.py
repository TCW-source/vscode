#樂透號碼判斷
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    CLS = []
    # 把 S 裡面的字串轉成數字，並檢查是否都在 1~49 內
    if all(1 <= int(ls) <= 49 for ls in LS) and len(set(LS)) == 7:
        print('Yes')
    else:
        print('No')

        
'''
    for ls in LS:
        ils = int(ls)
        if (ils >= 1 and ils <= 49) and (ils not in CLS):
            CLS.append(ils)
        else:
            print('NO')
            break

    if len(CLS) == 7:
        print('Yes')
'''