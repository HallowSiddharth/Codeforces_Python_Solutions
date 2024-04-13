t=int(input())
for i in range(t):
    n,k=list(map(int,input().rstrip().split()))
    a=list(map(int,input().rstrip().split()))
    b=list(map(int,input().rstrip().split()))
    b.sort(reverse=True)
    a.sort()
    c=[]
    for i in range(k):
        if b[i]>a[i]:
            c.append(b[i])
        else:
            c.append(a[i])
    c+=a[k:]
    print(sum(c))