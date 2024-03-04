class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj=defaultdict(list)
        for i,j in roads:
            adj[i].append(j)
            adj[j].append(i)
        mini=0
        vis=set()
        def dfs(src):
            nonlocal mini
            
            if src in vis:
                return 0
            vis.add(src)
            cost=0
            for v in adj[src]:
                cur=dfs(v)
                mini += (cur + seats -1)//seats
                cost += cur
            return cost + 1
        dfs(0)
        return mini


