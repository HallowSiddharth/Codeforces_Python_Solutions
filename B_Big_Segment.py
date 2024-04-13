n = int(input())
dx = {}
dy = {}
for i in range(n):
    x, y = list(map(int, input().rstrip().split()))
    if x in dx:
        dx[x] += 1
    if x not in dx:
        dx[x] = 1
    if y in dy:
        dy[y] += 1
    if y not in dy:
        dy[y] = 1
dxvalues = list(dx.values())
dyvalues = list(dy.values())

ma = max(max(dxvalues), max(dyvalues))

if ma != 1:
    print(ma)
else:
    print(-1)
