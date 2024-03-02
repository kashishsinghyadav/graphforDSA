class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n=len(bombs)
        adj=defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                x1=bombs[i][0]
                y1=bombs[i][1]
                r1=bombs[i][2]
                x2=bombs[j][0]
                y2=bombs[j][1]
                r2=bombs[j][2]
                dist=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
                if r1 >=dist:
                    adj[i].append(j)
        res=0
        vis=set()
        maxi=-1
       
        def dfs(src,vis):
            vis.add(src)
            for v in adj[src]:
                if v not in vis:
                    dfs(v,vis)

        for i in range(n):
            dfs(i,vis)
            count=len(vis)
            
            maxi=max(maxi,count)
            vis.clear()
        return maxi


