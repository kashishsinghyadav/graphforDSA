
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        q = []
        for i, j in adj.items():
            l = len(j)
            heappush(q, (-l, -i))
        heapify(q)
        print(q) 
        ans=[0]*(n)
        
        while q:
            val= heappop(q)
            ele=-val[-1]
            prio=-val[0]
            ans[ele]=n
            n-=1
        res=0
        for u,v in roads:
            val=ans[u]+ans[v]
            res+=val
        return res
