t = int(input())
for i in range(t):
    n,m,d = list(map(int,input().rstrip().split()))
    times = []
    occ = 1
    sellers = list(map(int,input().rstrip().split()))
    d = 2
    while occ<n :

        if occ in sellers or occ == 1:
            times.append(occ)
            d = 2
        
        elif d == 0:
            times.append(occ)
            d = 2
        
        else:
            d -= 1
            occ += 1
        