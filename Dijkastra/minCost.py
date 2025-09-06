

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        h = []
        heappush(h, (0, 0, 0)) 
        dirs = [(0,1), (0,-1), (1,0), (-1,0)] 

        visited = [[False for _ in range(n)] for _ in range(m)]

        while h:
            cost, r, c = heappop(h)

            if r == m-1 and c == n-1:
                return cost

            if visited[r][c]:
                continue

            visited[r][c] = True

            for i, (dr, dc) in enumerate(dirs):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    preferred_dir = grid[r][c] - 1  

                    if i == preferred_dir:
                        heappush(h, (cost, nr, nc))
                    else:
                        heappush(h, (cost + 1, nr, nc))
