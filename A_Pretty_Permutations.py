t = int(input())
for i in range(t):
    n = int(input())
    ans = False
    lst = []
    if n % 2 == 0:
        for i in range(1, n + 1, 2):
            lst.extend([i + 1, i])
    else:
        if n == 1:
            ans = True
            print(1)
        elif n == 3:
            ans = True
            print(3, 1, 2)
        else:
            lst.extend([3, 1, 2])
            for i in range(4, n, 2):
                lst.extend([i + 1, i])
    if not ans:
        lst = [str(i) for i in lst]
        print(" ".join(lst))
