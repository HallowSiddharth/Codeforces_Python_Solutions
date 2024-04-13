n,c=list(map(int,input().rstrip().split()))
lst=list(map(int,input().strip().split()))
d={}
for i in range(n):
    d[i+1]=lst[i]

i=1
ans=None

while True:
    if i not in d:
        pass
    else:
        d[i]-=c
        if d[i]<=0:
            del d[i]
            if d=={}:
                ans=i
                break
    i=(i+1)%(n+1)
    
print(ans)
