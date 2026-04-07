#時分秒
N = eval(input())
for i in range(N):
    sec = eval(input())
    S = sec%60
    min = sec//60
    M = min%60
    hr = min//60
    
    print(f'{hr:0>2}:{M:0>2}:{S:0>2}')
        

