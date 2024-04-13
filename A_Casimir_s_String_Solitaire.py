t=int(input())
for i in range(t):
    st=input()
    d={'A':0,'B':0,'C':0}
    for i in st:
        d[i]+=1
    if d['B']==d['A']+d['C']:
        print("YES")
    else:
        print("NO")