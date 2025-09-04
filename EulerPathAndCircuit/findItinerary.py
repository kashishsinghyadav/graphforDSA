class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
       
        for u,v in tickets:
            heapq.heappush(adj[u], v)
           

       
           
        res=[]
        def dfs(u):
            while adj[u]:
                node=heapq.heappop(adj[u])
                dfs(node)
            res.append(u)
        dfs("JFK")
        return res[::-1]
        
        

        
