class Solution:
    
    def spanningTree(self, V, adj):
        lst = []
        for u in range(V):
            for v, wt in adj[u]:
                lst.append((u, v, wt))
        
        newlst = sorted(lst, key=lambda x: x[2])
        parent = [i for i in range(V)]
        rank = [0 for _ in range(V)]
        
        def find(val):
            if parent[val] == val:
                return val
            parent[val] = find(parent[val])
            return parent[val]
                
        def union(u, v):
            paru = find(u)
            parv = find(v)
            if paru != parv:
                if rank[paru] < rank[parv]:
                    parent[paru] = parv
                elif rank[paru] > rank[parv]:
                    parent[parv] = paru
                else:
                    parent[paru] = parv
                    rank[parv] += 1
                
        s = 0
        edges_in_tree = 0
        for u, v, wt in newlst:
            if edges_in_tree == V - 1:  
                break
            p1 = find(u)
            p2 = find(v)
            if p1 != p2:
                union(u, v)
                s += wt
                edges_in_tree += 1
        return s
