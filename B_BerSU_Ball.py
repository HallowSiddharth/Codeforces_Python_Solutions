n = int(input())
lst = list(map(int, input().rstrip().split()))
m = int(input())
lst2 = list(map(int, input().rstrip().split()))
lst.sort()
lst2.sort()
ans = 0
if n > m:
    for i in range(len(lst2)):
        if lst2[i] - 1 in lst:
            lst.remove(lst2[i] - 1)
            ans += 1
        elif lst2[i] in lst:
            lst.remove(lst2[i])
            ans += 1
        elif lst2[i] + 1 in lst:
            lst.remove(lst2[i] + 1)
            ans += 1
        else:
            pass
else:
    for i in range(len(lst)):
        if lst[i] - 1 in lst2:
            lst2.remove(lst[i] - 1)
            ans += 1
        elif lst[i] in lst2:
            lst2.remove(lst[i])
            ans += 1
        elif lst[i] + 1 in lst2:
            lst2.remove(lst[i] + 1)
            ans += 1
        else:
            pass
print(ans)
