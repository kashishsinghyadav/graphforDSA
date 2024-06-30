

class Solution:
    def finddia(self, curr, parent, dist, res, adj):
        if dist > res[0]:
            res[0] = dist
            res[1] = curr
        for neb in adj[curr]:
            if neb != parent:
                self.finddia(neb, curr, dist + 1, res, adj)

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj1 = defaultdict(list)
        adj2 = defaultdict(list)
        
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        res1 = [-float('inf'), -1]
        res2 = [-float('inf'), -1]
        
        self.finddia(0, -1, 0, res1, adj1)
        self.finddia(res1[1], -1, 0, res2, adj1)
        dia1 = res2[0]
        
        res1 = [-float('inf'), -1]
        res2 = [-float('inf'), -1]
        
        self.finddia(0, -1, 0, res1, adj2)
        self.finddia(res1[1], -1, 0, res2, adj2)
        dia2 = res2[0]
        
        
        max_dia = max(dia1, dia2)
        
        return max(math.ceil(dia1/2)+math.ceil(dia2/2)+1, max_dia)
