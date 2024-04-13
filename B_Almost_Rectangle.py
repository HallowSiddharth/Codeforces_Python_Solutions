t = int(input())
for i in range(t):
    n = int(input())
    board = []
    stars = []
    for j in range(n):
        st = list(input())
        found = False
        if "*" in st:
            found = True
            ind = st.index("*")
            stars.append((j, ind))
        if found and "*" in st[ind + 1 :]:
            ind2 = st[ind + 1 :].index("*") + ind
            stars.append((j, st[ind + 1 :].index("*") + ind + 1))
        board.append(st)
    #print(stars)
    a = stars[0]
    b = stars[1]
    ax = a[0]
    ay = a[1]
    bx = b[0]
    by = b[1]
    if ax == bx:
        if ax != 0:
            board[ax - 1][ay] = "*"
            board[ax - 1][by] = "*"
        else:
            board[ax + 1][ay] = "*"
            board[ax + 1][by] = "*"
    elif ay == by:
        if ay != 0:
            board[ax][ay - 1] = "*"
            board[bx][ay - 1] = "*"
        else:
            board[ax][ay + 1] = "*"
            board[bx][ay + 1] = "*"
    else:
        board[bx][ay] = "*"
        board[ax][by] = "*"
    for _ in board:
        print("".join(_))
