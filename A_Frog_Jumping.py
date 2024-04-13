t=int(input())
for _ in range(t):
    a,b,k=list(map(int,input().rstrip().split()))
    if k%2==0:
        print((k//2)*(a-b))
    else:
        print((((k+1)//2)*a) - ((k//2))*b )