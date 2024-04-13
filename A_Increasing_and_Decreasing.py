t = int(input())
for _ in range(t):
    x, y, n = map(int, input().split())
    lst = [y]
    i = y
    j = 1
    while i - j > x:
        i -= j
        j += 1
        lst.append(i)

    lst = lst[::-1]
    # print(lst)
    if len(lst) >= n - 1:
        m = lst.pop(-1)
        lst = lst[-(n - 2) :]
        lst.append(m)
        lst.insert(0, x)
        if lst[1] - lst[0] == lst[-1] - lst[-2]:
            print(-1)
        else:
            print(*lst)

    else:
        print(-1)
