n = int(input())
lst = list(map(int, input().rstrip().split()))
wt = 0
d = {200: 0, 100: 0}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1


if d[200] % 2 != 0 and d[100] % 2 == 0 and d[100] > 1:
    print("YES")

elif d[200] % 2 == 0 and d[100] % 2 == 0:
    print("YES")

else:
    print("NO")
