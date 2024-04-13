t=int(input())
for _ in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    d={}
    for i in lst:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    m=-1
    for i in d:
        if d[i]==1 and m==-1:
            m=i
        elif d[i]==1 and i<m:
            m=i
    if m==-1:
        print(-1)
    else:
        print(lst.index(m)+1)
        