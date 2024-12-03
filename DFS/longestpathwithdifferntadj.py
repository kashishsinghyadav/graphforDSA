class Solution:
    def longestPath(self, p: List[int], s: str) -> int:
        n=len(p)
        adj=[[] for _ in range(n)]
        for v in range(1,n):
            adj[p[v]].append(v)
            adj[v].append(p[v])
       
        res=0
        def dfs(bacha,papa):
            nonlocal res
            longest=0
            slongest=0

            for child in adj[bacha]:
                if child==papa:
                    continue
                child_len=dfs(child,bacha)
                if s[child]==s[bacha]:
                    continue
                if child_len>slongest:
                    slongest=child_len
                if slongest>longest:
                    slongest,longest=longest,slongest
                
            onegood=max(slongest,longest)+1
            rootgood=1
            leafgood=1+slongest+longest
            res=max(res,max(max(onegood,rootgood),leafgood))
            return max(onegood,rootgood)



        dfs(0,-1)
        return res   
