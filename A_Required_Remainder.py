t=int(input())
for i in range(t):
    x,y,n=list(map(int,input().rstrip().split()))
    r=n%x
    if r<y:
        print(n-x+y-r)
    else:
        print(n-(r-y))