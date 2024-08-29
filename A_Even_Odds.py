import math

n, k = list(map(int, input().rstrip().split()))
mid = math.ceil(n / 2)

if k > mid:
    # even case
    print(2 * (k - mid))
else:
    # odd case
    print((2 * k) - 1)
