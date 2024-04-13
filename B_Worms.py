def juicy_binarysearch(nl,key,low,high):
    if high-low==1:

        # if key>nl[low]:
        #     return low+1
        # else:
        #     return low-1
        if key!=nl[high] and key!=nl[low]:
            if key>nl[high]:
                return high+1
            elif key<nl[high] and key>nl[low]:
                return high
            elif key<nl[low]:
                return low
    else:
        mid=low+high//2
        if key>nl[mid]:
            return juicy_binarysearch(nl,key,mid,high)
        elif key<nl[mid]:
            return juicy_binarysearch(nl,key,low,mid)
        else:
            return mid



n=int(input())
lst=list(map(int,input().rstrip().split()))
init=0
nl=[]
for i in range(n):
    init+=lst[i]
    nl.append(init)
t=int(input())
wormlist=list(map(int,input().rstrip().split()))
for i in wormlist:
    print(juicy_binarysearch(nl,i,0,n)+1)