t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    lst.sort()
    ans = 0
    for k in range(1, 101):
        i = 0
        j = n - 1
        ct = 0
        while i < j:
            if lst[i] + lst[j] == k:
                ct += 1
                i += 1
                j -= 1
            elif lst[i] + lst[j] < k:
                i += 1
            else:
                j -= 1
        if ct > ans:
            ans = ct
    print(ans)
