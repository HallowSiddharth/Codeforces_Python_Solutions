lst=list(map(int,input().rstrip().split()))
x4=max(lst)
lst.remove(x4)
x1,x2,x3=lst
print(x4-x1,x4-x2,x4-x3)