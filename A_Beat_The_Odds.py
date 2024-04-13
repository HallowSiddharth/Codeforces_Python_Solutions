t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    on=0
    en=0
    for i in lst:
        if i%2==0:
            en+=1
        else:
            on+=1
    print(min(on,en))