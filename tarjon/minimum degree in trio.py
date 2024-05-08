class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        arr=[[0 for _ in range(n+1)] for _ in range(n+1)]
      
        degree=[0]*(n+1)
        for u,v in edges:
            arr[u][v]=1
            arr[v][u]=1
            degree[u]+=1
            degree[v]+=1
        ans=1e9
        for i in range(1,n+1):
            
            for j in range(i+1,n+1):
                if arr[i][j]==1:

                    for k in range(j+1,n+1):
                        if arr[i][k]==1 and arr[j][k]==1:
                            ans=min(ans,degree[i]+degree[j]+degree[k]-6)
        if ans==1e9:
            return -1
        return ans
