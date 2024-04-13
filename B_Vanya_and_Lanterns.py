n, l = map(int, input().split())
lst = list(map(int, input().rstrip().split()))
lst.sort()
md = 0
md = max(md, lst[0] - 0)
for i in range(1, n):
    if (lst[i] - lst[i - 1]) / 2 > md:
        md = (lst[i] - lst[i - 1]) / 2
md = max(md, l - lst[-1])
print(md)
