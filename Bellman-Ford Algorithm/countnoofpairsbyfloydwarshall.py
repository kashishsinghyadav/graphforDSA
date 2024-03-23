class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        arr=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if abs(i-j)==1:
                    arr[i][j]=1
                elif i==j:
                    arr[i][j]=0
        arr[x][y]=1
        arr[y][x]=1
        
        for v in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    arr[i][j]=min(arr[i][j],arr[i][v]+arr[v][j])
        # print(arr)
        ans=[0]*(n+1)
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i!=j:
                    ans[arr[i][j]] +=1 
        return ans[1:]
        


        
