import math
d={i:float('inf') for i in ['A','B','C','AB','BC','AC','ABC']}
t=int(input())
for i in range(t):
    l=list(map(str,input().rstrip().split()))
    cost=int(l[0])
    vitamins=[j for j in l[1]]
    vitamins.sort()
    abc=''.join(vitamins)
    if abc=='A':
        if cost<d['A']:
            d['A']=cost
            d['AB']=min(d['A']+d['B'] , d['AB'])
            d['AC']=min(d['A']+d['C'] , d['AC'])
            d['ABC']=min(d['AB']+d['AC'],d['BC']+d['AC'],d['AB']+d['BC'],d['A']+d['B']+d['C'] ,d['AB']+d["C"],d['BC']+d['A'],d['AC']+d['B'], d['ABC'])
    elif abc=='B':
        if cost<d['B']:
            d['B']=cost
            d['AB']=min(d['A']+d['B'] , d['AB'])
            d['BC']=min(d['B']+d['C'],d['BC'])
            d['ABC']=min(d['AB']+d['AC'],d['BC']+d['AC'],d['AB']+d['BC'],d['A']+d['B']+d['C'] ,d['AB']+d["C"],d['BC']+d['A'],d['AC']+d['B'], d['ABC'])
    elif abc=='C':
        if cost<d['C']:
            d['C']=cost
            d['AC']=min(d['A']+d['C'] , d['AC'])
            d['BC']=min(d['B']+d['C'],d['BC'])
            d['ABC']=min(d['AB']+d['AC'],d['BC']+d['AC'],d['AB']+d['BC'],d['A']+d['B']+d['C'] ,d['AB']+d["C"],d['BC']+d['A'],d['AC']+d['B'], d['ABC'])

    elif abc=='AB':
        if cost<d['AB']:
            d['AB']=cost
            d['ABC']=min(d['AB']+d['AC'],d['BC']+d['AC'],d['AB']+d['BC'],d['A']+d['B']+d['C'] ,d['AB']+d["C"],d['BC']+d['A'],d['AC']+d['B'], d['ABC'])

    
    elif abc=='BC':
        if cost<d['BC']:
            d['BC']=cost
            d['ABC']=min(d['AB']+d['AC'],d['BC']+d['AC'],d['AB']+d['BC'],d['A']+d['B']+d['C'] ,d['AB']+d["C"],d['BC']+d['A'],d['AC']+d['B'], d['ABC'])

    elif abc=='AC':
        if cost<d['AC']:
            d['AC']=cost
            d['ABC']=min(d['AB']+d['AC'],d['BC']+d['AC'],d['AB']+d['BC'],d['A']+d['B']+d['C'] ,d['AB']+d["C"],d['BC']+d['A'],d['AC']+d['B'], d['ABC'])

    
    else:
        d['ABC']=min(cost,d['ABC'])


if d['ABC']==float('inf'):
    print(-1)
else:
    print(d['ABC'])

        

