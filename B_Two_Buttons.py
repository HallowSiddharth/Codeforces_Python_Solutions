import math
n,m=list(map(int,input().rstrip().split()))
if n>=m:
    print(n-m)
else:
    ans=0
    if n > m/2:
        if m%2==0:
            ans=1
            ans+=(n - m//2)
            print(ans)
        else:
            ans=1
            ans+=(n-math.ceil(m/2))
            ans+=1
            print(ans)
    elif n==m/2:
        print(1)
    else:
        ans=0
        while n<m/2:
            n=n*2
            if n>=m/2:
                ans+=1
                break
            else:
                n-=1
                ans+=2
        if m%2==0:
            ans+=1
            ans+=(n - m//2)
            print(ans)
        else:
            ans+=1
            ans+=(n-math.ceil(m/2))
            ans+=1
            print(ans)
