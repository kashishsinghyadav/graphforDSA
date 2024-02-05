from collections import deque
class Solution:
    def orangesRotting(self, grid) :

        row=len(grid)
        col=len(grid[0])
        queue=deque()
        fo=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    queue.append([i,j,0])
                elif grid[i][j]==1:
                    fo+=1
        print(queue)
        dirarr=[[-1,0],[0,-1],[0,1],[1,0]]
        mini=0
        while queue:
            nr,nc,t=queue.popleft()
            for d in dirarr:
                r=nr+d[0]
                c=nc+d[1]
                if (0<=r<row and 0<=c<col) and grid[r][c]==1:
                    queue.append([r,c,t+1])
                    grid[r][c]=2
                    mini=t+1
                    fo-=1

        return mini if fo==0 else -1
ans =Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(ans.orangesRotting(grid))