"""
Logic:
1. function keeps calling itself till 1, then swaps from 1 to n
2. so max element should be 1st element, then rest should be in ascending order
"""


n = int(input())
lst = [str(i) for i in range(1, n)]
print(str(n), " ".join(lst))
