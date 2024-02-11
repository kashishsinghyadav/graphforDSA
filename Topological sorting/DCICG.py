class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        v=len(prerequisites)
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)

        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j] += 1
        queue=[]
        for i in range(numCourses):
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
        if len(topo)==numCourses:
            return topo
        else:
            return []