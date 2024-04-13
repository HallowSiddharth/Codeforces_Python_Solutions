# t=int(input())
# for i in range(t):
#     n=int(input())
#     res=[0,0]
#     s=0
#     for i in range(n):
#         a,b=list(map(str,input().rstrip().split()))
#         if res==[1,1]:
#             continue
#         else:
#             if b=="01":
#                 res[1]=1
#             elif b=="10":
#                 res[0]=1
#             elif b=="11":
#                 res[0],res[1]=1,1
#             s+=int(a)
#             print(s)

#     print(s)
        

# t=int(input())
# for i in range(t):
#     n=int(input())
#     res=[0,0]
#     arr=[]
#     for i in range(n):
#         a,b=list(map(str,input().rstrip().split()))
#         arr.append([b,a])
#     arr.sort(reverse=True)
#     print(arr)
#     s=0
#     for i in range(n):
#         if res==[1,1]:
#             continue
#         else:
#             if arr[i][0]=="01":
#                 res[1]=1
#             elif arr[i][0]=="10":
#                 res[0]=1
#             elif arr[i][0]=="11":
#                 res[0],res[1]=1,1
#             s+=int(a)

#     print(s)



t=int(input())
for i in range(t):
    n=int(input())
    m_lst={0:[],1:[],2:[]}
    res=[0,0]
    s=0
    for i in range(n):
        a,b=list(map(str,input().rstrip().split()))
        if b=='01':
            if m_lst[0]==[] or m_lst[0][0]>a:
                m_lst[0]=[a,b]
        elif b=="10":
            if m_lst[1]==[] or m_lst[1][0]>a:
                m_lst[1]=[a,b]
        elif b=="11":
            if m_lst[2]==[] or m_lst[2][0]>a:
                m_lst[2]=[a,b]
    if m_lst[2]==[]:
        if m_lst[1]==[] or m_lst[0]==[]:
            print(-1)
        else:
            print(int(m_lst[1][0])+int(m_lst[0][0]))
    else:
        if m_lst[1]==[] or m_lst[0]==[]:
            print(m_lst[2][0])
        else:
            na=int(m_lst[1][0])+int(m_lst[0][0])
            nb=int(m_lst[2][0])
            if na>nb:
                print(nb)
            else:
                print(na)
