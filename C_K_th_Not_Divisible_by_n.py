import math

t = int(input())
for i in range(t):
    n, k = list(map(int, input().rstrip().split()))
    ans = k + int(k / (n - 1))
    if ans % n == 0:
        print(ans - 1)
    else:
        print(ans)
