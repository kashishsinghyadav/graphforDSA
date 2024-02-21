class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for v in flights:
            adj[v[0]].append((v[-1],v[1]))
        res=[float('inf')]*n
        res[src]=0
        q=[]
        heappush(q,(0,0,src))
        count=0
        vis={}
        while q:
            wt, stop, node= heappop(q)
            vis[node]=stop

            if node==dst:
                return wt
            if stop>k:
                continue

            for neb in adj[node]:
                weight_neb=neb[0]
                child_neb=neb[-1]
                if child_neb in vis and vis[child_neb]<=stop:
                    continue
                
                res[child_neb]=wt + weight_neb 
                heappush(q,(wt + weight_neb,stop+1,child_neb))
                  
            
        return -1


        
