t=int(input())
for i in range(t):
    n=int(input())
    st1=input()
    st2=input()
    lst1=[]
    lst2=[]
    for i in st1:
        if i=='G':
            lst1.append('B')
        else:
            lst1.append(i)
    
    for i in st2:
        if i=='G':
            lst2.append('B')
        else:
            lst2.append(i)
    
    if lst1==lst2:
        print("YES")
    else:
        print("NO")
        
        