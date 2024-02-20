class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[float('inf') for _ in range(n)] for _ in range(n)]

        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w

        for v in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j]=min(dist[i][j],dist[i][v]+dist[v][j])

        print(dist)
        ans=float('inf')
        
        idx=-1

        for i in range(n):
            count=0
            for j in range(n):
                if i!=j and dist[i][j]<=distanceThreshold:
                    count+=1
            if ans>=count:
                ans=count
                idx=i
        return idx

