"""
Already submitted, providing documentation
Logic:
1. given eqns : a²+b=n , a+b²=m
2. put b=0 (a,b >0) . max value of a = sqrt(n)
3. iterate over all possible values of a. using trail and error, find b
4. check second statement true. If yes, increase answer by 1
"""


import math
n, m = list(map(int, input().rstrip().split()))
ans = 0
for a in range(0, int(math.sqrt(n)) + 1):
    b = n - a**2
    if a + b**2 == m:
        ans += 1
print(ans)
