n,m,k=list(map(int,input().rstrip().split()))
mi=min(m,k)
if n<=mi:
    print("Yes")
else:
    print("No")