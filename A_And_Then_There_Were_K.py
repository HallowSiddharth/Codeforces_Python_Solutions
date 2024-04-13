import math

t = int(input())
for i in range(t):
    anss = 0
    n = int(input())
    group = math.log2(n)
    group = int(group)
    for power in range(group):
        anss += 2**power
    print(anss)
