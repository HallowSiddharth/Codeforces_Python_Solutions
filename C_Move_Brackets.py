t=int(input())
for i in range(t):
    l=int(input())
    st=input()
    stk=[]
    s=0
    for i in st:
        if i == '(':
            stk.append(i)
        else:
            if len(stk)!=0:
                stk.pop(-1)
    print(len(stk))
