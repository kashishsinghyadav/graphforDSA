class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n

        def dfs(color,graph,src,currc):
            color[src]=currc
            for v in graph[src]:
                if color[v]==color[src]:
                    return False
                if color[v]==-1:
                    color[v]=1-color[src]
                    if dfs(color,graph,v,color[v])==False:
                        return False
        for i in range(n):
            if  color[i]==-1:
                if dfs(color,graph,i,1)==False:
                    return False

        return True
        
