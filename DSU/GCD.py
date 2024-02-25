class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n=len(nums)
        parent=[i for i in range(n+1)]
        rank=[1]*(n+1)
        def find(val):
            if val==parent[val]:
                return val
            parent[val]=find(parent[val])
            return parent[val]
        def union(u,v):
            px=find(u)
            py=find(v)
            if px==py:
                return 
            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[px]<rank[py]:
                parent[px]=py
            else:
                parent[px]=py
                rank[py] += 1
        adj={}
        for i, num in enumerate(nums):
            if num == 1:
                return False
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    adj.setdefault(j, []).append(i)
                    k = num // j
                    if k == j:
                        continue
                    adj.setdefault(k, []).append(i)
            adj.setdefault(num, []).append(i)
        for factor, indices in adj.items():
            for i in range(len(indices) - 1):
                union(find(indices[i]), find(indices[i + 1]))

        count = 0
        for i in range(len(nums)):
            if find(i) == i:
                count += 1
            if count > 1:
                return False

        if count == 1:
            return True

        return False
