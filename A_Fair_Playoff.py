t = int(input())
for i in range(t):
    lst = list(map(int, input().rstrip().split()))
    if min(lst[:2]) < max(lst[2:]) and max(lst[:2]) > min(lst[2:]):
        print("YES")
    else:
        print("NO")
