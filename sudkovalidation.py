class Solution:
    def isValidSudoku(self, board):
        rows = []
        for i in board:
            rows.append(i)
        colums = [[] for _ in range(9)]

        for i in range(0, 9):
            for j in board:
                colums[i].append(j[i])
        # print(rows)
        # print(colums)
        ans = True
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column].isdigit():
                    el = board[row][column]
                    if rows[row].count(el) > 1 or colums[column].count(el) > 1:
                        ans = False
                    if self.boxcheck(el, row, column, board) == False:
                        ans = False

        return ans

    def boxcheck(self, el, row, colum, board):
        vertical = None
        horizontal = None
        if row in range(0, 3):
            vertical = 0
        elif row in range(3, 6):
            vertical = 3
        else:
            vertical = 6
        if colum in range(0, 3):
            horizontal = 0
        elif colum in range(3, 6):
            horizontal = 3
        else:
            horizontal = 6
        ans = True
        boxes = [[] for _ in range(9)]
        for i in range(vertical, vertical + 3):
            for j in range(horizontal, horizontal + 3):
                boxes[vertical // 3 + horizontal // 3].append(board[i][j])
                if board[i][j] == el and (i != row and j != colum):
                    ans = False
                    #print(boxes, el, row, colum)
        return ans


s = Solution()
print(
    s.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
