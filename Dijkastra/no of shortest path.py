class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj=defaultdict(list)
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))
        res=[float('inf')]*n  
        res[0]=0
        q=[]
        heappush(q,(0,0))
        noofway=[0]*n
        noofway[0]=1
        mod=10**9+7
        while q:
            wt,node=heappop(q)

            for neb in adj[node]:
                nod=neb[0]
                wegt=neb[-1]
                if wegt+wt < res[nod]:
                    res[nod]=wegt+wt 
                    noofway[nod]=noofway[node]
                    heappush(q,(res[nod],nod))
                elif wegt+wt == res[nod]:
                    noofway[nod]=(noofway[nod]+noofway[node])%mod

        return noofway[n-1]%mod
