d={}
j=0

for i in 'qwertyuiopasdfghjkl;zxcvbnm,./':
    d[i]=j
    j+=1

lst=[i for i in list(d.keys())]
ch=input()
stin=input()
st=''
if ch=='L':
    for i in stin:
        st+=lst[d[i]+1]
else:
    for i in stin:
        st+=lst[d[i]-1]
print(st)