t=int(input())
for i in range(t):
    st=input()
    lst=[]
    for i in range(len(st)):
        if st[i]=='1':
            lst.append(i)
    if lst==[] or len(lst)==1:
        print(0)
    else:
        s=0
        for j in st[lst[0] : lst [-1]+1]:
            if j=='0':
                s+=1

        print(s)        
