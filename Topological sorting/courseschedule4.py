class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], que: List[List[int]]) -> List[bool]:
        
        adj=[set() for _ in range(n)]
        indeg=[0]*n
        for u,v in pre:
            adj[u].add(v)
            indeg[v] += 1
        res=defaultdict(set)
        q=deque([])
        for i in range(len(indeg)):
            if indeg[i]==0:
                q.append(i)
        while q:
            curr=q.popleft()
            for neb in adj[curr]:
                res[neb].add(curr)
                res[neb].update(res[curr])
                indeg[neb]-=1
                if indeg[neb]==0:
                    q.append(neb)
        ans=[]
        for q in que:
            if q[0] in res[q[1]]:
                ans.append(True)
            else:
                ans.append(False)
        return ans
