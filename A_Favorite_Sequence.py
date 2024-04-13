t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    mid = len(lst) // 2
    lst1 = lst[: mid + 1]
    lst2 = lst[mid:]
    lst2 = lst2[::-1]
    ans = []
    for j in range(n):
        if j % 2 == 0:
            ans.append(lst1.pop(0))
        else:
            ans.append(lst2.pop(0))
    ans2 = [str(_) for _ in ans]
    print(" ".join(ans2))
