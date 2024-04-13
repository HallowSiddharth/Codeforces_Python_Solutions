t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    st = input()
    liked = []
    disliked = []
    for i in range(n):
        if st[i] == "1":
            liked.append(lst[i])
        else:
            disliked.append(lst[i])
    result = disliked + liked
    print(*result)
