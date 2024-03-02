class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        v=len(edges)
        adj=[[] for i in range(v)]
        for i in range(v):
            adj[i].append(edges[i])

        indegree=[0]*v
        for i in range(v):
            for j in adj[i]:
                indegree[j] += 1
        queue=[]
        for i in range(v):
            if indegree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            node = queue.pop(0)
            topo.append(node)

            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        ans=[0]*v
        for x in set(range(v))-set(topo): # it find the length of cycle 
            print(x)
            if ans[x]==0:
                val=[]
                while not val or x!=val[0]:
                    val.append(x)
                    x=edges[x]
                for x in val:
                    ans[x]=len(val)
      
        for x in topo: # the no of not not in the cycle
            stack=[]
            while ans[x]==0:
                stack.append(x)
                x=edges[x]
            while stack:
                ans[stack[-1]]=1+ans[x]
                x=stack.pop()
        return ans


       
