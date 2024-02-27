class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], prob: List[float], src: int, dest: int) -> float:
        res=[0]*n
        adj=[[] for _ in range(n)]
        for i, (u, v) in enumerate(edges):
            adj[u].append((v, prob[i]))
            adj[v].append((u, prob[i])) 
        

        res[src]=1
        q=[]
        heappush(q,(-1.0,src))
        while q:
            wt,node = heappop(q)
            newwt=-wt
            
            for neb in adj[node]:
                nod=neb[0]
                nwt=neb[-1]
                if newwt*nwt > res[nod]:
                    res[nod]=newwt*nwt
                    heappush(q,(-res[nod],nod))
            if node==dest:
                break
        return res[dest]
