t = int(input())
d = {}
import math

for i in range(t):
    n = int(input())
    sum = int(math.sqrt(n) + int(n ** (1 / 3))) - 1
    print(sum)
