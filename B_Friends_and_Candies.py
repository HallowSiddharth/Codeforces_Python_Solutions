t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    s = sum(lst)
    d = {}
    for val in lst:
        if val in d:
            d[val] += 1
        else:
            d[val] = 1
    if len(d) == 1:
        print(0)
    else:
        if s % n == 0:
            lst.sort(reverse=True)
            ns = 0
            count = 0
            for value in range(len(lst)):
                ns += lst[value]
                s -= lst[value]
                count += 1
                if ns >= s:
                    break
            print(count)

        else:
            print(-1)
