t=int(input())
for i in range(t):
    n=int(input())
    alst=list(map(int,input().rstrip().split()))
    blst=list(map(int,input().rstrip().split()))
    bmax=blst[n-1]
    amax=alst[n-1]
    result="Yes"
    for i in range(n):
        if max(alst[i],blst[i]) > max(amax,bmax) or min(alst[i],blst[i]) > min(amax,bmax):
            result="No"
    print(result)