t = int(input())
for _ in range(t):
    n, x = list(map(int, input().rstrip().split()))
    lst = list(map(int, input().rstrip().split()))
    ans = 0
    tct = 0
    temp = 0
    for i in lst:
        temp += i
        if temp % x == 0:
            if tct > ans:
                ans = tct
            tct = 0
            temp = i
        tct += 1
    if tct == 1:
        if lst[-1] % x == 0:
            ans = -1
        else:
            ans = max(tct,ans)
    else:
        ans = max(tct, ans)
    print(ans)
