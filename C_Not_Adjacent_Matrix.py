t = int(input())
for _ in range(t):
    n = int(input())
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    else:
        res = []
        for i in range(1,(n**2)+1,2):
            res.append(i)
        for i in range(2,(n**2)+1,2):
            res.append(i)
        for i in range(n):
            print(*res[i*n:(i+1)*n])