import math
t=int(input())
for i in range(t):
    n,k=list(map(int,input().rstrip().split()))
    if n<k:
        print(math.ceil(k/n))
    elif k<n:
        k2=math.ceil(n/k) * k
        print(math.ceil(k2/n))
    else:
        print(1)
