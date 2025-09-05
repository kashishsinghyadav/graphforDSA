class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        q = deque()
        vis = set()
        m = len(grid)
        n = len(grid[0])

        if grid[0][0] == 0:
            q.append((0, 0, health))
            vis.add((0, 0, health))
        else:
            q.append((0, 0, health-1))
            vis.add((0, 0, health-1))

        while q:
            r, c, curr = q.popleft()

            for i, j in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = r + i
                nc = c + j

                if 0 <= nr < m and 0 <= nc < n and curr >= 1:
                    next_health = curr-1 if grid[nr][nc] == 1 else curr

                    if nr == m-1 and nc == n-1 and next_health >= 1:
                        return True
                    if next_health >= 1 and (nr, nc, next_health) not in vis:
                        q.append((nr, nc, next_health))
                        vis.add((nr, nc, next_health))

        return False
