def split(n,m):
    if n%3!=0:
        if n==m:
            return "YES"
        else:
            return "NO"
    else:
        a=n//3
        b=n*2//3
        if m>a:
            return(split(b,m))
        else:
            return(split(a,m))



t=int(input())
for i in range(t):
    n,m=list(map(int,input().rstrip().split()))
    print(split(n,m))