class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        
        def dfs(src,vis,inrec,adj):
            vis[src]=True
            inrec[src]=True
            
            for nbr in adj[src]:
                
                if not vis[nbr] and dfs(nbr,vis,inrec,adj):
                    return True
                    
                elif inrec[nbr]:
                    return True
                    
            inrec[src]=False
            return False
        
        
        vis=[False]*V
        inrec=[False]*V
        
        for i in range(V):
            if not vis[i] and dfs(i,vis,inrec,adj):
                return True
                
        return False
