class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        m=len(h)
        n=len(h[0])
        pacific=[[0 for _ in range(n)] for _ in range(m)]
        atlantic=[[0 for _ in range(n)] for _ in range(m)]
        direction=[(-1,0),(0,-1),(1,0),(0,1)]
        q=deque([])
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    q.append((i,j))
                    pacific[i][j]=1
        q1=deque([])
        for i in range(m):
            for j in range(n):
                if i==m-1 or j==n-1:
                    q1.append((i,j))
                    atlantic[i][j]=1
        while q:
            ele=q.popleft()
            for r,c in direction:
                nr=ele[0]+r
                nc=ele[1]+c 
                if 0 <= nr < m and 0 <= nc < n and h[nr][nc] >= h[ele[0]][ele[1]] and pacific[nr][nc] != 1:

                    q.append((nr,nc))
                    pacific[nr][nc]=1
        # print(pacific)
        while q1:
            ele=q1.popleft()
            for r,c in direction:
                nr=ele[0]+r
                nc=ele[1]+c 
                if 0 <= nr < m and 0 <= nc < n and h[nr][nc] >= h[ele[0]][ele[1]] and atlantic[nr][nc] != 1:

                    q1.append((nr,nc))
                    atlantic[nr][nc]=1
        ans=[]
        for i in range(m):
            for j in range(n):
                if pacific[i][j]==1 and atlantic[i][j]==1:
                    ans.append([i,j])
        return ans

