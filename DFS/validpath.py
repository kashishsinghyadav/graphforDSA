class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, des: int) -> bool:
        vis=[False]*n
        ans=[]
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(src):
            vis[src]=True
            ans.append(src)
            for neb in adj[src]:
                if not vis[neb]:
                    dfs(neb)
            return ans

        dfs(src)
        if des in ans:
            return True
        return False
