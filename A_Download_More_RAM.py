t = int(input())
for i in range(t):
    n, k = list(map(int, input().rstrip().split()))
    alist = list(map(int, input().rstrip().split()))
    blist = list(map(int, input().rstrip().split()))
    d = {}
    together = []
    for i in range(n):
        together.append([alist[i], blist[i]])
    together = sorted(together, key=lambda a: a[0])
    total = k
    for a, b in together:
        if a <= total:
            total += b
        else:
            break
    print(total)
