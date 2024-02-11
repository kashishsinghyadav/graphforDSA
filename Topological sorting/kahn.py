from collections import deque

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        ans=[0]*V
        for i in range(V):
            for j in adj[i]:
                ans[j]+=1
                
        q=deque([])
        for i in range(len(ans)):
            if ans[i]==0:
                q.append(i)
                
        res=[]
                
        while q:
            u=q.popleft()
            res.append(u)
            for v in adj[u]:
                ans[v]-=1
                if ans[v]==0:
                    q.append(v)
                    
        return res
