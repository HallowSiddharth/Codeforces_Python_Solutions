n=int(input())
ans=1
master_list=[]
for i in range(n):
    lst=list(map(int,input().rstrip().split()))
    master_list.append(tuple(lst))

d={}

for i in master_list:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

print(max(list(d.values())))
