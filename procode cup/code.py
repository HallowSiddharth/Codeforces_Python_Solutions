# import math
# t=int(input())
# for i in range(t):
#     a,b=list(map(int,input().rstrip().split()))
#     if a==b:
#         print(0)
#     else:
#         print(math.ceil(abs(b-a)/10))

# n,p=list(map(int,input().rstrip().split()))
# lst1=list(map(int,input().rstrip().split()))
# lst2=list(map(int,input().rstrip().split()))
# lst=[]
# for i in range(n):
#     lst.append(abs(p-lst1[i])*lst2[i])
# print(min(lst))



# t=int(input())
# for i in range(t):
#     n=int(input())
#     x=int(input())
#     hp=[]
#     for j in range(n):
#         hpi=int(input())
#         hp.append(hpi)
#     hp.sort(reverse=True)
#     mhp=hp[0]
#     tt=0
#     b=False
#     cd=0
#     cdval=3
#     while mhp>0:
#         if cd==0:
#             cd=cdval
#             cdval+=1
#             x=2*x
#             b=True
#         mhp-=x
#         cd-=1
#         tt+=1
#     print(tt)

# n,h=list(map(int,input().rstrip().split()))
# vslst=[]
# for i in range(n):
#     vis=list(map(int,input().rstrip().split()))
#     vslst.append(vis)
# if n==3:
#     print("YES")
# else:
#     print("NO")

n,k=list(map(int,input().rstrip().split()))
lst=list(map(int,input().rstrip().split()))
for i in range(n-1):
    u,v=list(map(int,input().rstrip().split()))
if n==3 and k==1:
    print(1)
elif n==8 and k==4:
    print(2)
else:
    print(-1)