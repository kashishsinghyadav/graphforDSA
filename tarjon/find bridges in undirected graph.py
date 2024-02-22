# using tarjan algo
class Solution:
    def criticalConnections(self, n: int, conn: List[List[int]]) -> List[List[int]]:
        adj=[[] for _ in range(n)]
        for u in conn:
            adj[u[0]].append(u[1])
            adj[u[1]].append(u[0])
        disc=[-1]*n
        low=[-1]*n
        parent=-1
        vis=[False]*n
        def dfs(src,res,timer,parent):
            vis[src]=True
            timer+=1
            disc[src] = timer 
            low[src] = timer
           
            for neb in adj[src]:
                if neb==parent:
                    continue
                if not vis[neb]:
                    dfs(neb,res,timer,src)
                    low[src]=min(low[src],low[neb])
                    if low[neb]>disc[src]:
                        ans=[src,neb]
                        res.append(ans)
                        
                else:
                    low[src]=min(low[src],disc[neb])
            return res



        res=[]
        timer=0
        for i in range(n):
            if not vis[i]:
                dfs(i,res,timer,parent)
        return res
       

        
