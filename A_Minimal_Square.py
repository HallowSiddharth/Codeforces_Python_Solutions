t=int(input())
for i in range(t):
    a,b=list(map(int,input().rstrip().split()))
    a,b=max(a,b),min(a,b)
    if a<=b*2:
        print(b*2*b*2)
    else:
        print(a*a)