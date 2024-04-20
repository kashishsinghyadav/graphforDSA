

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        ans = []
        
        def bfs(row, col):
            min_row, min_col, max_row, max_col = row, col, row, col
            q = deque([(row, col)])  
            vis[row][col] = True

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1 and not vis[nr][nc]:
                        q.append((nr, nc))
                        vis[nr][nc] = True
                        min_row, min_col = min(min_row, nr), min(min_col, nc)
                        max_row, max_col = max(max_row, nr), max(max_col, nc)
            
            ans.append([min_row, min_col, max_row, max_col])
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and not vis[i][j]:
                    bfs(i, j)
        
        return ans
