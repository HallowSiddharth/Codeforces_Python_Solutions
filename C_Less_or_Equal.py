n, k = list(map(int, input().rstrip().split()))
d = {}
lst = list(map(int, input().rstrip().split()))


lst.sort()
if k == 0:
    if lst[0] > 1:
        print(lst[0] - 1)
    else:
        print(-1)
else:
    if lst.count(lst[k - 1]) > 1:
        if (k == n) or (k - 1 < n and lst[k] != lst[k-1]):
            print(lst[k-1])
        else:
            print(-1)
    else:
        print(lst[k - 1])
