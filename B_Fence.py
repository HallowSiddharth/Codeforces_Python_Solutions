n,k=list(map(int,input().rstrip().split()))
lst=list(map(int,input().rstrip().split()))
s=sum(lst[:k])
ans=1
for i in range(n-k):
    s1=sum(lst[i:i+k])
    if s1<s:
        ans=i+1

print(ans)
