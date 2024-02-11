class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        
        def dfs(src,vis,stack):
            vis[src]=True
            
            for v in adj[src]:
                if not vis[v]:
                    dfs(v,vis,stack)
                    
            stack.append(src)
            
            

        vis=[False]*V
        stack=[]
        
        for i in range(V):
            if not vis[i]:
                dfs(i,vis,stack)
                
        return stack[::-1]
