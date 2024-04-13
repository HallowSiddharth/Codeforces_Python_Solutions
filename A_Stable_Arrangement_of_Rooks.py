import math

t = int(input())
for i in range(t):
    n, k = list(map(int, input().rstrip().split()))
    board = [["." for column in range(n)] for row in range(n)]
    max_rooks = math.ceil(n / 2)
    rook_count = 0
    if k > max_rooks:
        print(-1)
    else:
        for r in range(0, n, 2):
            if rook_count < k:
                board[r][r] = "R"
                rook_count += 1
            else:
                break
        for row in board:
            print("".join(row))
