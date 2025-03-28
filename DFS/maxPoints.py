

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # dire = [(0,1), (1,0), (0,-1), (-1,0)]
        # m, n = len(grid), len(grid[0])

        # def bfs(vis, src, query):
        #     q = deque()  
        #     q.append(src)
        #     vis.add(src)
        #     cnt = 0 
        #     while q:
        #         e1, e2 = q.popleft()
        #         for r, c in dire:
        #             nr, nc = e1 + r, e2 + c
        #             if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in vis and grid[nr][nc] < query:
        #                 cnt += 1
        #                 q.append((nr, nc))
        #                 vis.add((nr, nc))
        #     return cnt
        
       
        # ans = []
        # for query in queries:
        #     if grid[0][0] < query:
        #         ans.append(bfs(set(), (0, 0), query)+1)
        #     else:
        #         ans.append(0)
        # return ans

        m, n = len(grid), len(grid[0])
        h = [(grid[0][0], 0, 0)]
        ans = [0] * len(queries)
        cnt = 0
        grid[0][0] = 0
        que = sorted(list(enumerate(queries)), key=lambda x: x[1])

        for k in range(len(que)):
            while h and h[0][0] < que[k][1]:
                _, r, c = heappop(h)
                cnt += 1
                for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nr = i + r
                    nc = j + c
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]:
                        heappush(h, (grid[nr][nc], nr, nc))
                        grid[nr][nc] = 0
            ans[que[k][0]] = cnt
        
        return ans
