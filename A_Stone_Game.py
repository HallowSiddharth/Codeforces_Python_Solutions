t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    maxel = max(lst)
    minel = min(lst)
    maxind = lst.index(maxel)
    minind = lst.index(minel)
    minfromright = n - minind
    maxfromright = n - maxind
    a1 = max(minind, maxind) + 1
    a2 = max(minfromright, maxfromright)
    a3 = min(maxind + minfromright, minind + maxfromright) + 1
    print(min(a1, a2, a3))
