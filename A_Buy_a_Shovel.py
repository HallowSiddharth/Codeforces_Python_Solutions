k,r=list(map(int,input().rstrip().split()))
s=1
ans=k
i=0
while True:
    if (ans-r)%10 ==0 or ans%10 ==0:
        break
    else:
        ans+=k
        s+=1
print(s)
