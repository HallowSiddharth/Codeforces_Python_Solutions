t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    print(max(lst)-min(lst))