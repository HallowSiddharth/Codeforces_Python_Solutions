t=int(input())
for i in range(t):
    n=int(input())
    lst=list(map(int,input().rstrip().split()))
    visited=[]
    extra=[]
    for i in lst:
        if i not in visited:
            visited.append(i)
        else:
            extra.append(i)
    s=0
    if len(extra)%2!=0:
        print(len(visited)-1)
    else:
        print(len(visited))