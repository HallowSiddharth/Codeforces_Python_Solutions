n=int(input())
lst=list(map(int,input().rstrip().split()))
d={}
for i in lst:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(max(list(d.values())),len(d))