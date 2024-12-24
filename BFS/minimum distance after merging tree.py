
class Solution:
    def findia(self, adj):
        node, _ = self.bfs(adj, 0)
        _, dia = self.bfs(adj, node)
        return dia

    def bfs(self, adj, src):
        q = deque()
        q.append(src)
        vis = set()
        vis.add(src)
        farthest_node = src
        max_dist = 0

        while q:
            l = len(q)
            for _ in range(l):
                curr_node = q.popleft()
                farthest_node = curr_node
                for neighbor in adj[curr_node]:
                    if neighbor not in vis:
                        q.append(neighbor)
                        vis.add(neighbor)
            if q:
                max_dist += 1

        return farthest_node, max_dist

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges1:
            adj[u].append(v)
            adj[v].append(u)

        adj1 = defaultdict(list)
        for u, v in edges2:
            adj1[u].append(v)
            adj1[v].append(u)

        dia1 = self.findia(adj)
        dia2 = self.findia(adj1)

        com = (dia1 + 1) // 2 + (dia2 + 1) // 2 + 1

        return max(dia1, dia2, com)
