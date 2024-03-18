

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in paths:
            adj[u].append(v)
            adj[v].append(u)
        print(adj)
        color = [0] * (n + 1)

        def dfs(src):
            for c in range(1, 5):  
                valid = True
                for neb in adj[src]:
                    if color[neb] == c:  
                        valid = False
                        break
                if valid:
                    color[src] = c  
                    break

        for i in range(1, n + 1):
            if color[i] == 0:
                dfs(i)

        return color[1:]
