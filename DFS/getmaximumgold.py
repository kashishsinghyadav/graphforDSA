class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        vis=set()
        m=len(grid)
        n=len(grid[0])

        def findpathwithmaxsum(st,end):
            if (st, end) in vis or st < 0 or st >= m or end < 0 or end >= n or grid[st][end] == 0:
                return 0

            vis.add((st,end))

            parent=grid[st][end]
            curr=0
            for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
                curr=max(curr,findpathwithmaxsum(st+i,end+j))
            vis.remove((st,end))
            return curr+parent



            




        res=-1e9    
        
        for i in range(m):
            for j in range(n):
               
                ans=findpathwithmaxsum(i,j)
                
                res=max(res,ans)

        return res

        
