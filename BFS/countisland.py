class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def check(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return True
            if grid2[i][j] != 1:
                return True
            
            grid2[i][j] = -1 
            
            res = True
            
            if grid1[i][j] == 0:
                res = False
            
            res = check(i + 1, j) and res
            res = check(i - 1, j) and res
            res = check(i, j + 1) and res
            res = check(i, j - 1) and res
            
            return res

        count = 0
        m = len(grid1)
        n = len(grid1[0])
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and check(i, j):
                    count += 1
        
        return count
