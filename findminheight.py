class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indegree=[0]*n 
        if n==1:
            return [0]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        q=deque([])
        for i in range(n):
            if indegree[i]==1:
                q.append(i)
                indegree[i]-=1
        ans=[]
        while q:
            l=len(q)
            ans=[]
            for i in range(l):
                curr=q.popleft()
                ans.append(curr)
                for neb in adj[curr]:
                    indegree[neb] -=1
                    if indegree[neb]==1:
                        q.append(neb)
        return ans



        
