t=int(input())
for i in range(t):
    n=int(input())
    d={}
    for _ in range(n):
        n1=int(input())
        lst=list(map(int,input().rstrip().split()))
        for j in lst:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
    finlst=[]
    for k in d:
        if d[k]==1:
            finlst.append(k)
    if len(finlst)==0:
        print(-1)
    else:
        finlst2=[str(k) for k in finlst]
        print(' '.join(finlst2))
     