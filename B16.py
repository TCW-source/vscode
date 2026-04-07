#汽水促銷活動
N = eval(input())
for i in range(N):
    n = int(input())
    total_drink = n
    bottles = n
    caps = n
    while bottles>=4 or caps>=3:
        if bottles >= 4:
            bottles = bottles-4
            total_drink+=1
            bottles+=1
            caps+=1
        elif caps>=3:
            caps = caps-3
            total_drink+=1
            bottles+=1
            caps+=1

    print(total_drink)