

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], src: int, dest: int, target: int) -> List[List[int]]:

        def dijkstra(ed, n, src, dest):
            adj = defaultdict(list)
            for u, v, w in edges:
                if w != -1:
                    adj[u].append((v, w))
                    adj[v].append((u, w))
            q = []
            heapq.heappush(q, (0, src))
            res = [float('inf') for i in range(n)]
            vis = [False for i in range(n)]
            res[src] = 0
            while q:
                wt, ele = heapq.heappop(q)
                if vis[ele]:
                    continue
                vis[ele] = True
                for neb in adj[ele]:
                    if neb[1] + wt < res[neb[0]]:
                        res[neb[0]] = neb[1] + wt
                        heapq.heappush(q, (res[neb[0]], neb[0]))
            return res[dest]

        findmin = dijkstra(edges, n, src, dest)
        if findmin < target:
            return []
        maxi = int(2e9)
        match = findmin == target
        if match:
            for i in range(len(edges)):
                if edges[i][2] == -1:
                    edges[i][2] = maxi
            return edges

        for i in range(len(edges)):
            if edges[i][2] == -1:
                if match:
                    edges[i][2] = maxi
                else:
                    edges[i][2] = 1
                if not match:
                    newdist = dijkstra(edges, n, src, dest)
                    if newdist <= target:
                        match = True
                        edges[i][2] += target - newdist

        if not match:
            return []
        return edges
