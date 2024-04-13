t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    ans = 1
    for j in range(len(lst) - 1):
        ans = max(ans, lst[j] * lst[j + 1])
    print(ans)
