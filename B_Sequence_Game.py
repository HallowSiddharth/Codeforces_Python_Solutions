t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().rstrip().split()))
    a = []
    a.append(b[0])
    for i in range(1, n):
        if b[i] < b[i - 1]:
            a.extend([b[i], b[i]])
        else:
            a.append(b[i])
    print(len(a))
    print(*a)
