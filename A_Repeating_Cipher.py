n=int(input())
st=input()
lst=[]
ini=0
for i in range(n):
    ini=ini+i
    lst.append(ini)
st2=''
for j in lst:
    if j<n:
        st2+=st[j]
print(st2) 
