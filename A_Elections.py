t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().rstrip().split()))
    ma = max(a, b, c)
    result = []
    ct = 0
    for el in [a,b,c]:
        if el == ma:
            ct += 1
    for j in [a, b, c]:
        if j != ma:
            result.append(ma - j + 1)
        elif j == ma and ct>1:
            result.append(1)
        else:
            result.append(0)
    result = [str(_) for _ in result]
    print(" ".join(result))
