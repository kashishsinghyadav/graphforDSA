# BFS+ DFS approach


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        vis = [[False for _ in range(n)] for _ in range(n)]
        q = deque([])

        def dfs(start, end):
            stack = [(start, end)]
            vis[start][end] = True
            q.append((start, end))
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = start + dr, end + dc
                if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc] and grid[nr][nc] == 1:
                    dfs(nr, nc)

        def bfs(q):
            count = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            if grid[nr][nc] == 1 and not vis[nr][nc]:
                                return count
                            elif grid[nr][nc] == 0 and not vis[nr][nc]:
                                q.append((nr, nc))
                                vis[nr][nc] = True
                count += 1
            return count

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return bfs(q)
