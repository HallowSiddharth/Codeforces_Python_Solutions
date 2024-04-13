n=int(input())
lst=list(map(int,input().rstrip().split()))
t=int(input())
l2=list(map(int,input().rstrip().split()))
d={'V':0,'P':0}
d2={}
for i in range(n):
    if lst[i] in d:
        d[lst[i]].append(i+1)
    else:
        d[lst[i]]=[i+1]

for i in l2:
    d['V']+=min(d[i])
    d['P']+=n-max(d[i]) +1 

print(d['V'],d['P'])