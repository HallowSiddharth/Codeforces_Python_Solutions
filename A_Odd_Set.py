t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    odd_c = 0
    eve_c = 0
    for i in lst:
        if i % 2 == 0:
            eve_c += 1
        else:
            odd_c += 1
    if odd_c == eve_c:
        print("Yes")
    else:
        print("No")
