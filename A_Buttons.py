import math

t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().rstrip().split()))
    if c // 2 + b >= a + math.ceil(c / 2):
        print("Second")
    else:
        print("First")
