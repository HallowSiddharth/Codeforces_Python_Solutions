import math
t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    print(math.ceil(sum(lst)/n))