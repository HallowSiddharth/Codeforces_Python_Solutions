n=int(input())
lst=list(map(int,input().rstrip().split()))
ma=max(lst)
s=0
for i in lst:
    s+=ma-i
print(s)