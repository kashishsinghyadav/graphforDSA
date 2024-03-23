

class Solution:
    def minimumCost(self, start, target, sr):
        
        mp = {}
        mp2 = {}
        c = 0
        
        if start[0] == target[0] and start[1] == target[1]:
            return 0
        
        if (start[0], start[1]) not in mp:
            mp[(start[0], start[1])] = c
            mp2[c] = (start[0], start[1])
            c += 1
        
        for s in sr:
            if (s[0], s[1]) not in mp:
                mp[(s[0], s[1])] = c
                mp2[c] = (s[0], s[1])
                c += 1
            if (s[2], s[3]) not in mp:
                mp[(s[2], s[3])] = c
                mp2[c] = (s[2], s[3])
                c += 1
        
        if (target[0], target[1]) not in mp:
            mp[(target[0], target[1])] = c
            mp2[c] = (target[0], target[1])
            c += 1
        
        adj = [[] for _ in range(c)]
        
        for i in range(c):
            for j in range(i + 1, c):
                dist = abs(mp2[i][0] - mp2[j][0]) + abs(mp2[i][1] - mp2[j][1])
                adj[i].append((j, dist))
                adj[j].append((i, dist))
        
        for s in sr:
            u = mp[(s[0], s[1])]
            v = mp[(s[2], s[3])]
            wt = s[4]
            
            for i in range(len(adj)):
                for j in range(len(adj[i])):
                    if i == u and adj[i][j][0] == v:
                        adj[i][j] = (v, min(adj[i][j][1], wt))
        
        pq = []
        dist = [float('inf')] * c
        dist[mp[(start[0], start[1])]] = 0
       
        heapq.heappush(pq, (0, mp[(start[0], start[1])]))
        vis = [False] * c
        
        while pq:
            d, u = heapq.heappop(pq)
            vis[u] = True
            
            for v, wt in adj[u]:
                if not vis[v] and dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, (dist[v], v))
        
        return dist[mp[(target[0], target[1])]]


