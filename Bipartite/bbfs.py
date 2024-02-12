class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        q=deque([])

        def bfs(q,color,graph,src,currc):
            
            q.append(src)
            color[src]=currc
            while q:
                curr=q.popleft()

                for v in graph[curr]:
                    if color[v]==color[curr]:
                        return False
                    if color[v]==-1:
                        color[v]=1-color[curr]
                        q.append(v)
            return True
        for i in range(n):
            if  color[i]==-1:
                if bfs(q,color,graph,i,1)==False:
                    return False

        return True
        
