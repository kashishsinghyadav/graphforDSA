class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(p,parent):
            if parent[p]==p:
                return p
            else:
                parent[p]=find(parent[p],parent)
                return parent[p]

        def union(x,y):
            px=parent[x]
            py=parent[y]
            if px==py:
                return 
            if rank[px]>rank[py]:
                parent[py]=parent[px]
            elif rank[px]<rank[py]:
                parent[px]=parent[py]
            else:
                parent[px]=parent[py]
                rank[py] += 1
        for v in edges:
            px=find(v[0],parent)
            py=find(v[1],parent)
            if px!=py:
                union(px,py)
            else:
                return [v[0],v[1]]

            

        
