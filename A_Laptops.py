n=int(input())
d={}
for i in range(n):
    a,b=list(map(int,input().rstrip().split()))
    d[a]=b
a2=list(d.keys())
a2.sort()
lst=[]
for i in a2:
    lst.append(d[i])
lst2=list(lst)
lst2.sort()
if lst == lst2:
    print("Poor Alex")
else:
    print("Happy Alex")