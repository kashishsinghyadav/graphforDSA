class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        parent=[i for i in range(len(row))]
        rank=[1]*len(row)
        def find(val):
            if val==parent[val]:
                return val
            parent[val]=find(parent[val])
            return parent[val]
        def union(x,y):
            px=find(x)
            py=find(y)
            if px!=py:
                if rank[px]>rank[py]:
                    parent[py]=px
                elif rank[px]<rank[py]:
                    parent[px]=py
                else:
                    parent[px]=py
                    rank[py]+=1
        for i in range(0,len(row),2):
            union(i,i+1)
        cnt=0
        for i in range(0,len(row),2):
            l=find(row[i])
            r=find(row[i+1])
            if l!=r:
                union(l,r)
                cnt+=1
        
        return cnt
        

        
          
