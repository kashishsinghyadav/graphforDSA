#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        vis=[False]*V
        ans=[]
        graph=[[] for _ in range(V)]
        
        for i in range(V):
            for j in adj[i]:
                graph[i].append(j)
                
        def solve(vis,graph,src,ans):
            vis[src]=True
            ans.append(src)
            
            for nbr in graph[src]:
                if not vis[nbr]:
                    solve(vis,graph,nbr,ans)
                
            
            
            
            
        
        solve(vis,graph,0,ans)
        return ans
