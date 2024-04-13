t = int(input())
for i in range(t):
    n = int(input())
    if n%2 == 0:
        ans = 0
    else:
        st = str(n)
        e = 0
        for j in st:
            if int(j)%2==0:
                e+=1
        if int(st[0])%2 == 0:
            ans = 1
        else:
            if e == 0:
                ans = -1
            else:
                ans = 2
    print(ans)