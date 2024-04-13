t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    s=0
    for i in lst:
        s+=i
    if s/n!=1:

        if s-n>0:
            print(s-n)
        else:
            print(1)
    else:
        print(0)