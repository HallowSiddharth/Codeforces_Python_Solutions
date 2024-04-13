import math

t = int(input())
for i in range(t):
    n = int(input())
    ans = math.ceil(n / 6)
    print(ans * 15)
