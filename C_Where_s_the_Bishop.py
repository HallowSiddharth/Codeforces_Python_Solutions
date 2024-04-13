t=int(input())
for i in range(t):
    board=[]
    input()
    for i in range(8):
        st=input()
        board.append([i for i in st])
    for j in range(1,7):
        if board[j-1].count('#')==2 and board[j+1].count('#')==2 and board[j].count('#')==1:
            ans=[j+1,board[j].index('#')+1]
    print(ans[0],ans[1])

