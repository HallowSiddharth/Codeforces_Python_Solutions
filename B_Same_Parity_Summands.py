t = int(input())
for _ in range(t):
    n, k = map(int, input().rstrip().split())
    if n % 2 == 1 and k % 2 == 1:
        ans = True
        arr = []
        for i in range(k - 1):
            if n > 0:
                n -= 1
                arr.append(1)
            else:
                ans = False
        if ans:
            if n > 0:
                arr.append(n)
            else:
                ans = False
        if ans:
            print("YES")
            print(*arr)
        else:
            print("NO")
    elif n % 2 == 0 and k % 2 == 1:
        ans = True
        arr = []
        for i in range(k - 1):
            if n > 0:
                n -= 2
                arr.append(2)
            else:
                ans = False
        if ans:
            if n > 0:
                arr.append(n)
            else:
                ans = False
        if ans:
            print("YES")
            print(*arr)
        else:
            print("NO")
    elif n % 2 == 0 and k % 2 == 0:
        ans = True
        arr = []
        for i in range(k - 1):
            if n > 0:
                n -= 1
                arr.append(1)
            else:
                ans = False
        if ans:
            if n > 0:
                arr.append(n)
            else:
                ans = False
        if ans:
            print("YES")
            print(*arr)
        else:
            print("NO")
    else:
        print("NO")
