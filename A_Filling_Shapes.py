n=int(input())
lst=[1,0]
for i in range(2,n+1):
    lst.append(2*lst[i-2])
print(lst[n])