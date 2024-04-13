n = int(input())
lst = list(map(int, input().rstrip().split()))
mi = min(lst)
ma = max(lst)

c_min = lst.count(mi)
c_ma = lst.count(ma)
if mi == ma:
    print(0, c_min * (c_min - 1) // 2)
else:
    print(ma - mi, c_ma * c_min)
