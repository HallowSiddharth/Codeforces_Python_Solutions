t = int(input())
for i in range(t):
    n, h = list(map(int, input().rstrip().split()))
    lst = list(map(int, input().rstrip().split()))
    el = max(lst)
    lst.remove(el)
    el2 = max(lst)
    start = 0
    while h > 0:
        if start % 2 == 0:
            h -= el
        else:
            h -= el2
        start += 1
    print(start)
