t = int(input())
import math

for i in range(t):
    n, m = list(map(int, input().rstrip().split()))
    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        if n % 2 == 0:
            print(math.floor(m * 1.5))
        else:
            print(math.floor(m * 2))
