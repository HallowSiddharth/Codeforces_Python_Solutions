t=int(input())
for i in range(t):
    n=int(input())
    st=input()
    lst=[i for i in st]
    lst.sort()
    d={}
    j=1
    for i in "abcdefghijklmnopqrstuvwxyz":
        d[i]=j
        j+=1
    print(d[lst[-1]])