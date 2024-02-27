class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj=[[] for _ in range(n)]
        indegree=[0]*n
        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1
        q=deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        ans=[set() for _ in range(n)]
        while q:
            curr=q.popleft()
            for neb in adj[curr]:
                ans[neb].add(curr)
                ans[neb].update(ans[curr])
                indegree[neb]-=1
                if indegree[neb]==0:
                    q.append(neb)

        res=[sorted(i) for i in ans]
        return res
