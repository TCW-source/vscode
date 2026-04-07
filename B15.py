#質數
N = eval(input())
for i in range(N):
    Target = int(input())
    CT = 0
    num = 2
    while CT < Target:
        is_prime = True
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                is_prime = False
                break
        
        if is_prime:
            CT += 1
            if CT == Target:
                print(num)
                break
        num += 1