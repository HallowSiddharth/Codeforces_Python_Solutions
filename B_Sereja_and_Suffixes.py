n,m=list(map(int,input().rstrip().split()))
arr=list(map(int,input().rstrip().split()))
lst=[]
for i in range(m):
    li=int(input())
    lst.append(li)
d={}
newlst=[]
for i in range(n-1,-1,-1):

    if newlst==[]:
        newlst.append(arr[i])
        d[i+1]=1

    else:
        if arr[i] in newlst:
            d[i+1]=d[i+2]
            
        else:
            d[i+1]=d[i+2]+1
        
        newlst.append(arr[i])

for i in lst:
    print(d[i])
