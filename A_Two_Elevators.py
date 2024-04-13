t=int(input())
for i in range(t):
    a,b,c=list(map(int,input().rstrip().split()))
    time2=abs(b-c)+abs(c-1)
    if a-1>time2:
        print(2)
    elif a-1<time2:
        print(1)
    else:
        print(3)