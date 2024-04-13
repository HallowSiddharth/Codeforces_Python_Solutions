n=int(input())
lst=list(map(int,input().rstrip().split()))
d={}
for i in lst:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
ma=0
for i in d:
    if d[i]>ma:
        ma=d[i]
if n%2==0:
    if ma<=n//2:
        print("YES")
    else:
        print("NO")
else:
    if ma<=(n//2)+1:
        print("YES")
    else:
        print("NO")