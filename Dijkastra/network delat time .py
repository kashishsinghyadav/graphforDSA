import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in times:
            u, v, w = i[0], i[1], i[2]
            if u not in adj:
                adj[u] = []
            adj[u].append([v, w])

        res = [float('inf')] * (n + 1)
        res[k] = 0
        q = []
        q.append([0, k])

        while q:
            dis, node = heapq.heappop(q)

            for v in adj.get(node, []):
                nn, nw = v[0], v[1]
                if dis + nw < res[nn]:
                    res[nn] = dis + nw
                    heapq.heappush(q, [res[nn], nn])

        if res.count(float('inf')) > 1:
            return -1
        else:
            return max(res[1:])
