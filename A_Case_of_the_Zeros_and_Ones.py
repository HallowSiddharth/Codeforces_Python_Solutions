n=int(input())
st=input()
st2=''
for i in range(len(st)-2):
    if (st[i]=='0' and st[i+1]=='1') or (st[i]=='1' and st[i+1]=='0'):
        pass
    else:
        st2+=st[i]
print(st2)


