t=int(input())
for i in range(t):
    m=0
    b=0
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    for i in lst:
        if i%2==0:
            m+=i
        else:
            b+=i
    if m>b:
        print("YES")
    else:
        print("NO")