class Solution:

    #Function to detect cycle using DSU in an undirected graph.
	def detectCycle(self, V, adj):
	    parent=[i for i in range(V)]
	    rank=[1 for i in range(V)]
	    def find(val,parent):
	        if parent[val]==val:
	            return val
	            
	        else:
	            parent[val]=find(parent[val],parent)
	            return parent[val]
	            
	    def union(x,y,parent,rank):
	        px=parent[x]
	        py=parent[y]
	        if px==py:
	            return 
	        if rank[px]>rank[py]:
	            parent[py]=parent[px]
	            
	        elif rank[px]<rank[py]:
	            parent[py]=parent[px]
	        else:
	            parent[px]=parent[py]
	            rank[py]+=1
	            
	            
	            
		
		
		for  u in range(V):
		    for v in adj[u]:
		        if v>u:
		            px=find(u,parent)
		            py=find(v,parent)
		            if px==py:
		                return 1
		            else:
		                union(px,py,parent,rank)
	    return 0
