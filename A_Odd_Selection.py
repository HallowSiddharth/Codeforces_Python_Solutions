t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    lst = list(map(int, input().rstrip().split()))
    d = {0: 0, 1: 0}
    for i in lst:
        if i % 2 == 0:
            d[0] += 1
        else:
            d[1] += 1
    ans = "No"
    for i in range(1, d[1] + 1, 2):
        if x - i < 0:
            break
        if (d[0] >= x - i):
            ans = "Yes"
    print(ans)
