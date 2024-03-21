class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        def findParent(parent , u) :
            if parent[u] == u : 
                return u 
            return findParent(parent , parent[u])

        n = len(edges) 
        parent = [i for i in range(n+1)] 
        cand1 , cand2 , visited = None , None , {}
        for x, y in edges :
            if y in visited :
                cand1,cand2 = visited[y] , [x,y]
                break 
            visited[y] = [x,y]
        
        for x,y in edges :
            if [x,y] == cand2 : continue 
            a = findParent(parent , x) 
            b = findParent(parent , y) 

            if(a == b) :
                if cand1 : return cand1 
                return [x,y]
            parent[b] = a
        return cand2
