class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        def dfs(i,j,vis):
            vis.add((i,j))
            temp=grid[i][j]

            for r,c in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                nr=i+r
                nc=j+c
                if 0<=nc<m and 0<=nr<n and grid[nr][nc]>0 and (nr,nc) not in vis:
                    temp += dfs(nr,nc,vis)
                
            return temp

        n=len(grid)
        m=len(grid[0])
        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]>0:
                    res=dfs(i,j,set())
                    ans=max(ans,res)
        return ans
        
