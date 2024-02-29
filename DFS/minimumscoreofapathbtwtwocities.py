class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        vis=[False]*(n+1)
       

        def dfs(src,res):

            vis[src]=True

            for v in adj[src]:
                neb=v[0]
                dist=v[-1]
                res=min(res,dist)
                if not vis[neb]:
                    res=dfs(neb,res)
            return res
        return dfs(1,float('inf'))
