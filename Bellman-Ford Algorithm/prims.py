#User function Template for python3
import  heapq 
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        q=[]
        q.append((0,0))
        vis=[False]*V
        s=0
        
        while q:
            wt,node=heapq.heappop(q)
            if  vis[node]:
                continue
            vis[node]=True
            s+=wt
            
            for v in adj[node]:
                neb=v[0]
                weg=v[1]
                if vis[neb]==False:
                    heapq.heappush(q,(weg,neb))
        return s
                    
                
