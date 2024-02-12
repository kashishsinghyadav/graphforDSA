class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        adj=[[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])

        q=deque([])
        vis=[False]*n
       
        res=[]
        ans=[]
        def bfs(src):
            ans=[]
            q.append(src)
            vis[src]=True

            

            while q:

                

                curr=q.popleft()
                ans.append(curr)
                

                for v in adj[curr]:
                    if not vis[v]:
                        q.append(v)
                        
                        vis[v]=True

            return ans
                

        for i in range(n):
            if not vis[i]:
                
                res.append(bfs(i))
                

        if len(res)==1:
            return 0
        
        else:

            v=0
            l=n
            for i in res:
                v+=len(i)*(l-len(i))
                l=l-len(i)
            return v

            

        
