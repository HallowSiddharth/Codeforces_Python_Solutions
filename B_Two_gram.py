t=int(input())
st=input()
ansind=0
ct2=0
for i in range(len(st)-1):
    ct=st.count(st[i:i+2])
    if ct>ct2:
        ct2=ct
        ansind=i
print(st[ansind:ansind+2])