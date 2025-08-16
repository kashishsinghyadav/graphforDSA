class Solution:
	def isEulerCircuitExist(self, V, adj):
		#Code here
		vis=[False]*V
		def dfs(st,vis):
		    vis[st]=True
		    
		    for neb in adj[st]:
		        if not vis[neb]:
		            dfs(neb,vis)
		            
        for i in range(V):
            if len(adj[i])!=0:
                dfs(i,vis)
                break
        for i in range(len(vis)):
            if not vis[i] and len(adj[i])>0:
                return 0
        odddeg=0    
        for i in range(V):
            if len(adj[i])%2!=0:
                odddeg += 1
        if odddeg > 2:
            return 0
        elif odddeg==2:
            return 1
        else:
            return 2
            
