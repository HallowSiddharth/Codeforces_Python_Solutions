st=input()
t=int(input())
for i in range(t):
    l,r=list(map(int,input().rstrip().split()))
    ans=0
    temp=st[0]
    for i in range(l-1,r-1):
        if st[i]==st[i+1]:
            ans+=1
    print(ans)

