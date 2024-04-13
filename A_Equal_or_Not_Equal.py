t = int(input())
for i in range(t):
    st = input()
    d = {}
    for j in st:
        if j in d:
            d[j] += 1
        else:
            d[j] = 1
    if len(d) == 1:
        print("YES")
    else:
        if d["E"] == 1 or d["N"] == 1:
            if st[0] != st[-1]:
                print("NO")
            else:
                print("YES")
        else:
            print("YES")
