#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        stack=[]
        vis=[False]*V
        def topo(src,stack,vis):
            vis[src]=True
            
            for v in adj[src]:
                if not vis[v]:
                    topo(v,stack,vis)
                    
            stack.append(src)
            return stack
            
        for i in range(V):
            if not vis[i]:
                topo(i,stack,vis)
        newgraph=[[] for _ in range(V)]
        for u in range(V):
            for v in adj[u]:
                newgraph[v].append(u)
                
        def dfs(src,g,newvis):
            newvis[src]=True
            for v in g[src]:
                if not newvis[v]:
                    dfs(v,g,newvis)
            
                
        count=0
        newvis=[False]*V
        while stack:
            val=stack.pop()
            if not newvis[val]:
                dfs(val,newgraph,newvis)
                count+=1 
        return count
                
