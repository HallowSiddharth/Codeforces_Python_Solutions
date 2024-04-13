t = int(input())
for i in range(t):
    lst = list(map(int, input().rstrip().split()))
    lst.sort()
    if lst[1] + lst[2] >= 10:
        print("YES")
    else:
        print("NO")
