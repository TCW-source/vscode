#質數
N = eval(input())
for i in range(N):
    n = int(input())
    is_prime = True
    for j in range(2, int(n**0.5)+1):
        if n % j == 0:
            is_prime = False
            break
    if is_prime:
        print(f'{n}: YES')
    else:
        print(f'{n}: NO')
