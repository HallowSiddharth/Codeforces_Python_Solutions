t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    lst.sort(reverse=True)
    # lst2 = list(lst)
    # dummy = [0 for _ in range(lst[0])]

    # for i in lst2:
    #     for j in range(i):
    #         dummy[j] += 1
    # if lst == dummy:
    #     print("YES")
    # else:
    #     print("NO")
    if n == lst[0]:
        print("YES")
    else:
        print("NO")
