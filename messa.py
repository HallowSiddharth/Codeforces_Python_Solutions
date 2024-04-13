a='abcdefghijklmnopqrstuvwxyz'
d={}
i=1
for j in a:
    d[j]=i
    i+=1
st=''
phrase="Royal Challengers Bangalore"
su=0
lst=[]
for i in phrase:
    if i==' ':
        continue
    k=i.lower()
    st+=f"{i} = {d[k]}\n"
    lst.append(str(d[k]))
    su+=d[k]
print(st)
with open('rcb.txt','w') as file:
    file.write(st)
    file.write('\n')
    file.write('+'.join(lst))
print(su)
