#道路修復工
N = eval(input())
for i in range(N):
    LS = input().split(' ')
    n = int(LS[0])
    r = int(LS[1])
    LX = input().split(' ')
    if n == r:
        print('*')
    else:
        LA = []
        for j in range(1,n+1): #準備所有清單1~n
            LA.append(str(j))
        for lx in LX: #倖存者列表
            if lx in LA:
                LA.remove(lx) #移出元素的值
        RV=''
        for la in LA:
            RV += f'{la} '
        print(RV)


