

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        adj = defaultdict(list)
        
        def dfs(curr, visited):
            visited[ord(curr) - ord('a')] = 1
            minChar = curr
            
            for v in adj[curr]:
                if visited[ord(v) - ord('a')] == 0:
                    minChar = min(minChar, dfs(v, visited))
            
            return minChar
        
        n = len(s1)
        for i in range(n):
            u = s1[i]
            v = s2[i]
            
            adj[u].append(v)
            adj[v].append(u)
        
        m = len(baseStr)
        result = ''
        
        for ch in baseStr:
            visited = [0] * 26
            result += dfs(ch, visited)
        
        return result
