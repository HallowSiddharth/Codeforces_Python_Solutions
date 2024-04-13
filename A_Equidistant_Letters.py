t = int(input())
for i in range(t):
    st = input()
    d = {}
    for val in st:
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
    ans1 = ''
    ans2 = ''
    for data in d:
        if d[data] == 2:
            ans1 += data
        else:
            ans2 += data
    print(ans1+ans1+ans2) 