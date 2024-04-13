t=int(input())
for i in range(t):
    n=int(input())
    st=input()
    st2=''
    for j in st:
        if j=='U':
            st2+='D'
        elif j=='D':
            st2+='U'
        else:
            st2+=j
    print(st2)