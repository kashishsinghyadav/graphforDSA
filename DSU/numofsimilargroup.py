class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        adj=defaultdict(list)
        def similar(s1,s2):
            m=len(s1)
            diff=0
            for i in range(m):
                if s1[i]!=s2[i]:
                    diff+=1
            if diff==2 or diff==0:
                return True
            return False
       
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
                parent[py]=px
                rank[px]+=1
        group=n
        for i in range(n):
            for j in range(i,n):
                if similar(strs[i],strs[j]) and find(i)!=find(j):
                    union(i,j)
                    group-=1
        return group
