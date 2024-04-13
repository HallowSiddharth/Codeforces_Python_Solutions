n=int(input())
lst=list(map(int,input().rstrip().split()))
d={50:0,25:0,100:0}
ans="YES"
for i in lst:
    if i==25:
        d[i]+=1
    elif i==50:
        if d[25]>=1:
            d[25]-=1
            d[50]+=1
        else:
            ans="NO"
            break
    else:
        if (d[50]>=1 and d[25]>=1) or (d[25]>=3):
            if (d[50]>=1 and d[25]>=1):
                d[i]+=1
                d[50]-=1
                d[25]-=1
            else:
                d[25]-=3
                d[i]+=1

        else:
            ans="NO"
            break
print(ans)