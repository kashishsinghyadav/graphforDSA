class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for ed in edges:
            adj[ed[0]].append(ed[1])
            adj[ed[1]].append(ed[0])
        
        ans = [0] * n
        dp = [1] * n
        
        def dfs(par, node, depth):
            ans[node] = depth
            for child in adj[node]:
                if child != par:
                    dfs(node, child, depth + 1)
                    dp[node] += dp[child]
                    ans[node] += ans[child]
        
        def dfs2(par, node, n):
            for child in adj[node]:
                if child != par:
                    ans[child] = ans[node] - dp[child] + (n - dp[child])
                    dfs2(node, child, n)
        
        dfs(0, 0, 0)
        dfs2(0, 0, n)
        
        return ans

