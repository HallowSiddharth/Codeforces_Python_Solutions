dx={}
dy={}
n=int(input())
points=[]

for i in range(n):
    lst=list(map(int,input().rstrip().split()))
    x=lst[0]
    y=lst[1]
    if x in dx:
        dx[x].append(y)
    else:
        dx[x]=[y]
    if y in dy:
        dy[y].append(x)
    else:
        dy[y]=[x]
    coords=tuple(lst)
    points.append(coords)

sp=0
for(x,y) in points:
    mix=min(dy[y])
    maax=max(dy[y])
    miy=min(dx[x])
    may=max(dx[x])
    if mix < x and maax > x and may > y and miy < y:
        sp+=1

print(sp)
