# n, m = list(map(int, input().rstrip().split()))
# board = []
# for i in range(n):
#     lst = list(input())
#     board.append(lst)
# for i in range(n):
#     for j in range(m):
#         if board[i][j] == ".":
#             ans = "W"
#             result = True
#             # print(j)
#             if j >= 1:
#                 # print(board[i][j - 1])
#                 if board[i][j - 1] == ans:
#                     result = False
#             if j < (n - 1):
#                 # print(board[i][j + 1])
#                 if board[i][j + 1] == ans:
#                     result = False
#             if i >= 1:
#                 # print(board[i - 1][j])
#                 if board[i - 1][j] == ans:
#                     result = False
#             if i < (n - 1):
#                 # print(board[i + 1][j])
#                 if board[i + 1][j] == ans:
#                     result = False
#             # print(result)
#             if result:
#                 board[i][j] = ans
#             else:
#                 board[i][j] = "B"
# for k in board:
#     print("".join(k))


n, m = list(map(int, input().rstrip().split()))
board = []
for i in range(n):
    lst = list(input())
    board.append(lst)
for i in range(n):
    for j in range(m):
        if board[i][j] == ".":
            if i % 2 == 0 and j % 2 == 0:
                board[i][j] = "B"
            elif i % 2 == 0 and j % 2 == 1:
                board[i][j] = "W"
            elif i % 2 == 1 and j % 2 == 0:
                board[i][j] = "W"
            else:
                board[i][j] = "B"

for k in board:
    print("".join(k))
