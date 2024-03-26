class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restrict=set(restricted)
        vis=set()
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        # print(adj)
        # print(restrict)
        cnt=1
       
        arr=set()
        def dfs(src):
            nonlocal cnt
            

            vis.add(src)
            for neb in adj[src]:
                if neb not in vis and neb not in restrict:
                    cnt+=1
                    dfs(neb)
        dfs(0)
        return cnt
