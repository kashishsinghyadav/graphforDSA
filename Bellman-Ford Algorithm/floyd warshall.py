class Solution:
	def shortest_distance(self, grid):
		#Code here
		n=len(grid)
		for i in range(n):
		    for j in range(n):
		        if grid[i][j]==-1:
		            grid[i][j]=100000
		            
        for v in range(n):
            for i in range(n):
                for j in range(n):
                    grid[i][j]=min(grid[i][j],grid[i][v]+grid[v][j])
                    
        for i in range(n):
		    for j in range(n):
		        if grid[i][j]==100000:
		            grid[i][j]=-1
