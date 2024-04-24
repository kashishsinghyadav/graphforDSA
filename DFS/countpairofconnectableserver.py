class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], ss: int) -> List[int]:
        adj=defaultdict(list)
        n=len(edges)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        ans=[]
        cnt=0
        def dfs(node,parent,wt):
            nonlocal cnt
            if wt%ss==0:
                cnt+=1
            for ch,dis in adj[node]:
                if ch!=parent:
                    dfs(ch,node,wt+dis)

        ans=[0 for i  in range(n+1)]
        for i in range(n+1):
            res=0
            s=0
            temp=[]
            for neb,wt in adj[i]:
                cnt=0
                dfs(neb,i,wt)
                temp.append(cnt)
                s+=cnt
            for ele in temp:
                res+=(s-ele)*ele
            ans[i]=res//2
        return ans


            
        
