t = int(input())
for i in range(t):
    a,b = list(map(int,input().rstrip().split()))
    total = a+b
    print(min(total//4, min(a,b)))