

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(colors)
        indeg = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            indeg[v] += 1
        
        vis = [[0] * 26 for _ in range(n)]
        
        q = deque([])
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
                vis[i][ord(colors[i]) - ord('a')] = 1
        
        maxi = 0
        count = 0
        while q:
            curr = q.popleft()
            count += 1
            maxi = max(maxi, max(vis[curr]))
            for neb in adj[curr]:
                for c in range(26):
                    vis[neb][c] = max(vis[neb][c], vis[curr][c] + (ord(colors[neb]) - ord('a') == c))
                indeg[neb] -= 1
                if indeg[neb] == 0:
                    q.append(neb)
        
        if count < n:
            return -1
        return maxi
