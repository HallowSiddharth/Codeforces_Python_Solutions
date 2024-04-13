t = int(input())
for _ in range(t):
    n, m = list(map(int, input().rstrip().split()))
    board = [[] for k in range(m)]
    for i in range(n):
        st = input()
        for j in range(len(st)):
            board[j].append(st[j])
    chars = ["v", "i", "k", "a"]
    for i in board:
        if chars == []:
            break
        elif chars[0] in i:
            chars.pop(0)
    if chars == []:
        print("YES")
    else:
        print("NO")
