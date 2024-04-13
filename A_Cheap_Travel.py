n,m,a,b=list(map(int,input().rstrip().split()))
import math
if b/m>=a:
    print(a*n)

elif a>b:
    print(math.ceil(n/m)*b) 

else:
    if m>n and a*n>=b:
        print(b)
    else:
        qo=n//m
        rem=n%m
        print((qo*b)+(rem*a))