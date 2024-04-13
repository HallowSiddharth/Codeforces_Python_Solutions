t=int(input())
for i in range(t):
    n=int(input())
    st=list(input())
    mi=st[0]
    for i in st:
        if mi>i:
            mi=i
    ind=st.index(mi)
    print(ind)
    st[0],st[ind]=st[ind],st[0]
    print(''.join(st))
