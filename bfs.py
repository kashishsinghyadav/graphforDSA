from collections import deque
class Graph:

    def buildlist(self,edges,n):
        g=[]
        for i in range(n):
            g.append(list())
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])

        return g
    def bfs(self,edges,n,src):
        g=self.buildlist(edges,n)
        vis=[False]*n
        vis[src]=True
        queue=deque()
        ans=[]
        queue.append(src)
        idx=0
        while queue:
            ele=queue.popleft()
            ans.append(ele)
            for nbr in g[ele]:
                if vis[nbr] is not True:
                    vis[nbr]=True
                    queue.append(nbr)

        return ans





edges = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 5], [3, 4], [3, 5]]
n = 6
src = 0
answer=Graph()
node=answer.bfs(edges,n,src)
for i in node:
    print(i,end=" ")
