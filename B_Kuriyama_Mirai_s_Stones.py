n = int(input())
lst = list(map(int, input().rstrip().split()))
lst2 = sorted(lst)
d1 = {}
d2 = {}
d1[1] = lst[0]
d2[1] = lst2[0]
for i in range(1, n):
    d1[i + 1] = d1[i] + lst[i]
for i in range(1, n):
    d2[i + 1] = d2[i] + lst2[i]
m = int(input())
for _ in range(m):
    qt, l, r = map(int, input().split())
    if qt == 1:
        if l != 1:
            print(d1[r] - d1[l - 1])
        else:
            print(d1[r])
    else:
        if l != 1:
            print(d2[r] - d2[l - 1])
        else:
            print(d2[r])
