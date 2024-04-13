t=int(input())
for i in range(t):
    n,q=list(map(int,input().rstrip().split()))
    lst=list(map(int,input().rstrip().split()))
    s=sum(lst)
    for i in range(q):
        l,r,k=list(map(int,input().rstrip().split()))
        ksum=k*(l-r+1)
        l-=1
        r-=1
        osum=0
        for j in range(l,r+1):
            osum+=lst[j]
        if s%2==0 and ((osum%2==0 and ksum%2==1) or (osum%2==1 and ksum%2==0)):
            print("YES")
        elif s%2==1 and ((osum%2==1 and ksum%2==1) or (osum%2==0 and ksum%2==0)):
            print("YES")
        else:
            print("NO")


