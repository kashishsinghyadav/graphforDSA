class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        vis=set()
        h=[]
        if grid[0][0]==1:
            heappush(h,(1,0,0,k-1))
            vis.add((0,0,k-1))
        else:
            heappush(h,(0,0,0,k))
            vis.add((0,0,k))
        m=len(grid)
        n=len(grid[0])
        
        while h:
            st,r,c,remain=heappop(h)
            if remain<0:
                continue
            if r==m-1 and c==n-1:
                return st
            for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr = i + r
                nc = j + c
                if 0<=nr<m and 0<=nc<n:
                    nremain=remain-grid[nr][nc]
                    if (nr,nc,nremain) not in vis and nremain>=0:
                        heappush(h,(st+1,nr,nc,nremain))
                        vis.add((nr,nc,nremain))
        return -1        
