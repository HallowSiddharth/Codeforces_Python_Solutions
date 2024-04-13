# t=int(input())
# for i in range(t):
#     n=int(input())
#     lst=list(map(int,input().rstrip().split()))
#     d={1:0,2:0}
#     for i in lst:
#         d[i]+=1
#     if d[1]%2==0 and d[1]>0:
#         print("YES")
#     else:
#         print("NO")




# 1 1 2 2 2
# 1 2 1 2
# 1 2 2 2

t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    tot=0
    d={1:0,2:0}
    for i in lst:
        d[i]+=1
        tot+=i
    if tot%2!=0:
        print("NO")
    else:
        if d[2]%2!=0 and d[1]==0:
            print("NO")
        else:
            print("YES")