n=int(input())
ans=False
res=[]
occ=False
for i in range(n):
    st=input()
    if not occ:
        if st=='OO|OX' or st=='OO|XO' or st=='OO|XX':
            res.append('++'+st[2:])
            occ=True
            ans=True
        elif st=="OX|OO" or st=="XO|OO" or st=="XX|OO":
            res.append(st[:3]+'++')
            occ=True
            ans=True
        elif st=="OO|OO":
            res.append("++|OO")
            occ=True
            ans=True
        else:
            res.append(st)
    else:
        res.append(st)
if ans==False:
    print("NO")
else:
    print("YES")
    for i in res:
        print(i)