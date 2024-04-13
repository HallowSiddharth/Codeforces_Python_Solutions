t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    d = {}
    for data in lst:
        if abs(data) not in d or data == 0:
            d[abs(data)] = 1
        else:
            if d[abs(data)] < 2:
                d[abs(data)] += 1
    print(sum(list(d.values())))
