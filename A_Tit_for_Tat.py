t = int(input())
for i in range(t):
    n, k = list(map(int, input().rstrip().split()))
    lst = list(map(int, input().rstrip().split()))
    m = 0
    while k > 0 and n - 1 > m:
        if k >= lst[m]:
            lst[-1] += lst[m]
            k -= lst[m]
            lst[m] = 0
            m += 1
        else:
            lst[-1] += k
            lst[m] -= k
            k = 0

    l2 = [str(_) for _ in lst]
    print(" ".join(l2))
