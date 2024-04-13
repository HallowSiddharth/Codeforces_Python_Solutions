t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    for j in range(n):
        lst2=list(map(str,input().rstrip().split()))
        for k in lst2[1]:
            if k=='D':
                lst[j]=(lst[j]+1)%10
            else:
                if lst[j]==0:
                    lst[j]=9
                else:
                    lst[j]-=1
    lst3=[str(m) for m in lst]
    print(' '.join(lst3))