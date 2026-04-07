#兩數相加
def two(nums , target) :
    n = len(nums)
    for j in range(i+1 , n):
        if nums[i] + nums[j] == target:
            return f"{i} {j}"


N = eval(input())
for i in range(N):
    X = input()
    Y = eval(input())
    ZLS = input().split(' ')
    Z = [int(s) for s in ZLS]
    
    result = two(Z,Y)
    print(result)