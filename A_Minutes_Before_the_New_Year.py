t=int(input())
for i in range(t):
    h,m=list(map(int,input().rstrip().split()))
    rh=23-h
    rm=60-m  
    print(rh*60 + rm)