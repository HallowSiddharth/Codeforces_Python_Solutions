t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().rstrip().split()))
    mi = min(a, b)
    ma = max(a, b)
    ans = False
    value = ma - mi
    if ma > value and mi <= value:
        total = value * 2
        if total >= c:
            if c + value > total:
                print((c + value) % (value * 2))
            else:
                print(c + value)
            ans = True
    if not ans:
        print(-1)
