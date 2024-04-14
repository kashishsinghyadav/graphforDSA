
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        res = [float('inf')] * n
        res[0] = 0
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        q = []
        heappush(q, (0, 0))
        while q:
            wt, ele = heappop(q)
            
            
            if wt==res[ele]:

                for neb in adj[ele]:
                    nebadj, nebwt = neb[0], neb[1]
                    if wt + nebwt < disappear[nebadj] and  wt + nebwt < res[nebadj]:
                        res[nebadj] = wt + nebwt
                        heappush(q, (res[nebadj], nebadj))
        for i in range(n):
            if res[i] == float('inf'):
                res[i] = -1
        return res
