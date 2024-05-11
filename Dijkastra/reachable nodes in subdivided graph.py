class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        g = [[-1] * n for _ in range(n)]

        for e in edges:
            g[e[0]][e[1]] = e[2]
            g[e[1]][e[0]] = e[2]

        ans = 0
        visited = [False] * n
        pq = [(-maxMoves, 0)]  

        while pq:
            m, u = heapq.heappop(pq)
            m= -m

            if visited[u]:
                continue

            visited[u] = True
            ans += 1

            for v in range(n):
                if g[u][v] != -1:
                    if not visited[v] and m >= g[u][v] + 1:
                        heapq.heappush(pq, (-(m - g[u][v] - 1), v))

                    mc = min(m, g[u][v])

                    g[v][u] -= mc
                    g[u][v] -= mc

                    ans += mc

        return ans
