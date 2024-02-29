class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        if n==1:
            return  0
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        q=[]
        heappush(q,(0,n))
        res=[float(inf)]*(n+1)
        res[n]=0
        while q:
            wt,node=heappop(q)
            for neb in adj[node]:
                dist=neb[-1]
                child=neb[0]
                if dist+wt<res[child]:
                    res[child]=dist+wt
                    heappush(q,(dist+wt,child))
       
        mod=10**9+7
        @lru_cache(None)
        def dfs(start):
            nonlocal mod
            
            if start==n:
                return 1
            ans=0
            for neb,_ in adj[start]:
                if res[start]>res[neb]:
                    ans = (ans +dfs(neb))%mod
            return ans
        return dfs(1)
        
