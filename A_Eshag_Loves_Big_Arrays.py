t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    d = {}
    for el in lst:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1
    if len(d) == 1:
        print(0)
    else:
        mi = min(lst)
        print(n - d[mi])
