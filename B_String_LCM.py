t=int(input())
for i in range(t):
    st1=input()
    st2=input()
    ost1=st1
    ost2=st2
    while len(st1)!=len(st2):
        if len(st1)<len(st2):
            st1+=ost1
        else: 
            st2+=ost2
    if st1==st2:
        print(st1)
    else:
        print(-1)