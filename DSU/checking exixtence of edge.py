class Solution:
    def distanceLimitedPathsExist(self, n: int, ed: List[List[int]], que: List[List[int]]) -> List[bool]:
        m=len(que)
        for i in range(m):
            que[i].append(i)
        newq=sorted(que,key=lambda x:x[2])
        newed=sorted(ed,key=lambda x:x[2])
        res=[False]*m
        parent=[i for i in range(n)]
        rank=[1]*n
        def find(val):
            if parent[val]==val:
                return val
            parent[val]=find(parent[val])
            return parent[val]
        def union(x,y):
            px=find(x)
            py=find(y)
            if px==py:
                return 
            if rank[px]<rank[py]:
                parent[px]=py
            elif rank[px]>rank[py]:
                parent[py]=px
            else:
                parent[px]=py
                rank[py]+=1
        j=0
        for i in range(m):
            q=newq[i]
            u=q[0]
            v=q[1]
            t=q[2]
            idx=q[3]
            while j<len(newed) and newed[j][2]<t:
                union(newed[j][0],newed[j][1])
                j+=1
            if find(u)==find(v):
                res[idx]=True
            else:
                res[idx]=False
        return res
        
