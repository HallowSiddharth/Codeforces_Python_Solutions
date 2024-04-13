n=int(input())
lst=list(map(int,input().rstrip().split()))
ind=0
while n>0:
    n-=lst[ind]
    ind=(ind+1)%7
if ind==0:
    print(7)
else:
    print(ind)
