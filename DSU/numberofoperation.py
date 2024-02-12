class Solution:
    def makeConnected(self, n: int, conn: List[List[int]]) -> int:
        if len(conn)<n-1:
            return -1
        
        rank=[0]*n
        parent =[i for i in range(n)]
        
        def find(p):
            if parent[p]==p:
                return p
            else:
                parent[p]=find(parent[p])
                return parent[p]

        def union(x,y):
            px=find(x)
            py=find(y)
            if px==py:
                return 

            if rank[px]<rank[py]:
                parent[px]=parent[py]
            elif rank[px]>rank[py]:
                parent[py]=parent[px]
            else:
                parent[px]=parent[py]
                rank[py] += 1
        count=n

        for v in conn:
            if find(v[0])!=find(v[1]):
                union(v[0],v[1])
                count-=1
        return count-1
