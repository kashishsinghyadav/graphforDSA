
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dp = {}
        mod = 10 ** 9 + 7
        direct = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(st, end):
            if (st, end) in dp:
                return dp[(st, end)]
            ans = 1
            for dir in direct:
                news = dir[0] + st
                newend = dir[1] + end
                if 0 <= news < m and 0 <= newend < n and grid[news][newend] > grid[st][end]:
                    ans = (ans + dfs(news, newend)) % mod
            dp[(st, end)] = ans
            return dp[(st, end)]

        result = 1
        for i in range(m):
            for j in range(n):
                result += dfs(i, j)
        return result % mod
