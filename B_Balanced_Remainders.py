t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    d = {0: 0, 1: 0, 2: 0}
    for i in lst:
        d[i % 3] += 1
    a = n // 3
    ans = 0
    if d[0] == min(d[1], d[2], d[0]):
        ans += 2 * (a - d[1])
        ans += a - d[0]
    elif d[1] == max(d[1], d[2], d[0]):
        ans += 2 * (a - d[0])
        ans += a - d[2]
    else:
        ans += 2 * (a - d[1])
        ans += a - d[0]
    print(ans)
