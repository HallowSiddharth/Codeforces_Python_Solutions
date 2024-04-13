t=int(input())
for _ in range(t):
    w=input()
    p=int(input())
    i=1
    d={}
    for j in 'abcdefghijklmnopqrstuvwxyz':
        d[j]=i
        i+=1
    lst=[k for k in w]
    s=0
    for i in lst:
        s+=d[i]
    lst.sort(reverse=True)
    if s<=p:
        print(w)
    else:
        while s>p:
            a=lst.pop(0)
            s-=d[a]
        st2=''
        for i in w:
            if i in lst:
                lst.remove(i)
                st2+=i
        print(st2)
