t = int(input())
for i in range(t):
    n, s = list(map(int, input().rstrip().split()))
    rem = n // 2 + 1
    print(s // rem)
