#今天星期幾
import datetime

def solve():
    try:
        h = int(input())
        for _ in range(h):
            y, m, d = map(int, input().split())
            # isoweekday() 直接回傳 1(一) 到 7(日)
            print(datetime.date(y, m, d).isoweekday())
    except EOFError:
        pass

solve()