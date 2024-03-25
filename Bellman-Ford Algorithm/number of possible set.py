class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans = 0

        for subset in range(1 << n):
            grid = [[10**9] * n for _ in range(n)]
            for u, v, wt in roads:
                if (subset >> u) & 1 and (subset >> v) & 1:
                    grid[u][v] = min(grid[u][v], wt)
                    grid[v][u] = min(grid[v][u], wt)

            for j in range(n):
                grid[j][j] = 0

            for via in range(n):
                for x in range(n):
                    for y in range(n):
                        grid[x][y] = min(grid[x][y], grid[x][via] + grid[via][y])

            ok = all(grid[j][k] <= maxDistance for j in range(n) for k in range(n) if j != k and (subset >> j) & 1 and (subset >> k) & 1)

            ans += 1 if ok else 0

        return ans
