from collections import deque
class Solution:
 #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, src):
        #code here
        res=[float('inf')]*V
        q=deque([])
        res[src]=0
        q.append([0,src])
        while q:
            curr=q.popleft()
            node=curr[-1]
            wt=curr[0]
            for v in adj[node]:
                adjn=v[0]
                adjw=v[-1]
                if wt+adjw < res[adjn]:
                    res[adjn]=wt+adjw
                    q.append([wt+adjw,adjn])
        return res
        
        
            
