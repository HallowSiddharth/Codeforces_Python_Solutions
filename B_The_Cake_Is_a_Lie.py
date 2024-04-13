# referred youtube for this answer
t = int(input())
for i in range(t):
    n, m, k = list(map(int, input().rstrip().split()))
    ma = max(n, m)
    mi = min(n, m)
    if n * m - 1 == k:
        print("YES")
    else:
        print("NO")
