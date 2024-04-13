d={'H':0,'C':0,'D':0,'S':0}
d2={i:0 for i in '23456789TJQKA'}
table=input()
suit=table[1]
card=table[0]
lst=list(map(str,input().rstrip().split()))
for i in lst:
    d[i[1]]+=1
    d2[i[0]]+=1

if d[suit]!=0 or d2[card]!=0:
    print("YES")
else:
    print("NO")