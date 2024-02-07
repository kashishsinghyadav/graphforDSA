from collections import deque
class Solution:
    def solve(self, board) -> None:
        row=len(board)
        col=len(board[0])
        queue=deque()
       
        dirarr=[[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(row):
            for j in range(col):
                if i==0 or i==row-1 or j==0 or j==col-1:
                    if board[i][j]=='O':
                        queue.append([i,j])
                       
                        board[i][j]='V'

        while queue:
            r,c=queue.popleft()
            for d in dirarr:
                nr=d[0]+r
                nc=d[1]+c
                if 0<=nr<row and 0<=nc<col and board[nr][nc]=='O':
                    queue.append([nr,nc])
                    board[nr][nc]='V'

        for i in range(row):
            for j in range(col):
                if board[i][j]=='V':
                    board[i][j]='O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

        
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
A= Solution()
print(A.solve(board))
