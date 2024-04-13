import math
for i in range(2,100001):
    pl=[2]
    d={}
    res=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            res=False
            break

print("DONE")
