import math 
t=int(input())
for i in range(t):
    n,m=list(map(int,input().rstrip().split()))
    print(math.ceil(n*m/2))