class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = [i for i in range(n)]
        cost = [-1] * n

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[y] = x

        for edge in edges:
            u, v, w = edge
            parent_u = find(u)
            parent_v = find(v)

            if parent_u != parent_v:
                cost[parent_u] &= cost[parent_v]
                union(parent_u, parent_v)

            cost[parent_u] &= w

        res = []
        for q in query:
            s, t = q
            p1 = find(s)
            p2 = find(t)

            if s == t:
                res.append(0)
            elif p1 != p2:
                res.append(-1)
            else:
                res.append(cost[p1])

        return res
