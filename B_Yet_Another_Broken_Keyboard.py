n,k=list(map(int,input().rstrip().split()))
st=input()
kn=list(map(str,input().rstrip().split()))
ans=[]
for i in st:
    if i in kn:
        ans.append(1)
    else:
        ans.append(0)
for i in range(1,n):
    if ans[i]!=0:
        ans[i]+=ans[i-1]
print(sum(ans))