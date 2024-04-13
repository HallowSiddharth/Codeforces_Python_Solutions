t=int(input())
for i in range(t):
    n,k=list(map(int,input().rstrip().split()))
    if k%2==n%2:
        print("YES")
    else:
        print("NO")