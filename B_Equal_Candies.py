t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    mi=min(lst)
    s=0
    for i in lst:
        s+= i-mi
    print(s)