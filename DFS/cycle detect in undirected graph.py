from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		def dfs(src,vis,adj,parent):
		    vis[src]=True
		    
		    for nbr in adj[src]:
		        if nbr==parent:
		            continue
		        if vis[nbr]:
		            return True
		            
		        if dfs(nbr,vis,adj,src):
		            return True
	        return False
		
		
		vis=[False]*V
		for i in range(V):
		    if not vis[i]:
		        if dfs(i,vis,adj,-1):
		            return True
	    return False
		    
