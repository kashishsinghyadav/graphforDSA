class Solution:
    def dfs(self,src,ans,adj):
        while adj[src]:             
            neb = adj[src].pop()
            self.dfs(neb, ans, adj)
        ans.append(src)
        
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj=defaultdict(list)
        indeg=defaultdict(int)
        outdeg=defaultdict(int)
        
        for u,v in pairs:
            adj[u].append(v)
            indeg[v]+=1
            outdeg[u]+=1
        
        st=pairs[0][0]
        for node in adj:
            if outdeg[node]-indeg[node]==1:
                st=node
                break

        res=[]
        self.dfs(st,res,adj)
        print(res)
        res=res[::-1]
        ans_pairs = [[res[i], res[i+1]] for i in range(len(res)-1)]
        return ans_pairs

        
        

        
    
