
#also done by bfs
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1.0 / value

        def dfs(start, end, visited):
            if start not in graph:
                return -1.0
            if end == start:
                return 1.0
            if end in graph[start]:
                return graph[start][end]

            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            return -1.0

        results = []
        for dividend, divisor in queries:
            visited = set()
            results.append(dfs(dividend, divisor, visited))

        return results
