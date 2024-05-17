class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]:
            return 0
        q=deque([])
        d={}
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j,0))
                    d[(i,j)]=0
        while q:
            r,c,w=q.popleft()
            neb=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for r1,c1 in neb:
                if (r1,c1) not in d and min(r1,c1)>=0 and max(r1,c1)<n:
                    d[(r1,c1)]=w+1
                    q.append((r1,c1,w+1))
        heap=[]
        heappush(heap,(-d[(0,0)],0,0))
        vis=set()
        vis.add((0,0))
        while heap:
            dist,r,c = heappop(heap)
            dist=-dist
            if (r,c) == (n-1,n-1):
                return dist
            neb=[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            for r1,c1 in neb:
                if (r1,c1) not in vis and  min(r1,c1)>=0 and max(r1,c1)<n:
                    mini=min(dist,d[(r1,c1)])
                    heappush(heap,(-mini,r1,c1))
                    vis.add((r1,c1))
        
            


        
