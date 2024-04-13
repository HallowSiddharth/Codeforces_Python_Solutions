t=int(input())
lst=[]
for j in [1,2,3,4,5,6,7,8,9,10]:
    for i in range(1,5):
        lst.append(str(j)*i)

for i in range(t):
    s=input()
    su=0
    for i in lst:
        if i==s:
            su+=len(i)
            break
        else:
            su+=len(i)
    print(su)