n = int(input())
lst = list(map(int, input().rstrip().split()))
d = {}


def checkap(lst):
    if len(lst) == 1:
        return 0
    else:
        ans = True
        cd = lst[1] - lst[0]
        for i in range(2, len(lst)):
            if lst[i] - lst[i - 1] != cd:
                ans = False
        if ans:
            return cd
        else:
            return -1


for i in range(n):
    if lst[i] in d:
        d[lst[i]].append(i)
    else:
        d[lst[i]] = [i]

lst2 = []
for i in d:
    statement = checkap(d[i])
    if statement != -1:
        lst2.append([i, statement])
lst2.sort()
print(len(lst2))
for i in lst2:
    print(i[0], i[1])
