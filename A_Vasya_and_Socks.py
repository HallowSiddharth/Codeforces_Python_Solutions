n,m=list(map(int,input().rstrip().split()))
ans=0
while n>0:
    n-=1
    ans+=1
    if ans%m==0:
        n+=1
print(ans)