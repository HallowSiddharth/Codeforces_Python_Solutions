n = int(input())
lst = list(map(int, input().rstrip().split()))
total = 0
for i in lst:
    total += i
print(total / n)
