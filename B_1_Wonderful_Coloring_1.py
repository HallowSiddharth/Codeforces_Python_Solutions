t = int(input())
for i in range(t):
    st = input()
    d = {}
    for val in st:
        if val in d:
            if d[val] == 2:
                continue
            else:
                d[val] += 1
        else:
            d[val] = 1
    vals = list(d.values())
    print(sum(vals) // 2)
