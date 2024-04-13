n,m=list(map(int,input().rstrip().split()))
lst=list(map(int,input().rstrip().split()))
s=0
for i in range(len(lst)-1):
    if i==0:
        s+=lst[i]-1
    if lst[i]<=lst[i+1]:
        s+=lst[i+1]-lst[i]
    else:
        s+=n-lst[i] + lst[i+1]
print(s)