t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    lst.sort()
    # if n%2==1:
    #     a=lst[:n//2]
    #     b=lst[n//2:]
    #     m1=b[0]-a[-1]
    #     c=lst[:n//2+1]
    #     d=lst[n//2+1:]
    #     m2=d[0]-c[-1]
    #     print(min(m1,m2))
    # else:
    #     a=lst[:n//2]
    #     b=lst[n//2:]
    #     print(b[0]-a[-1])   
    mi=lst[1]-lst[0]
    for i in range(1,len(lst)):
        if lst[i]-lst[i-1]<mi:
            mi=lst[i]-lst[i-1]

    print(mi)