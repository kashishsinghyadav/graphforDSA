class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        adj=defaultdict(list)
        def similar(s1,s2):
            m=len(s1)
            diff=0
            for i in range(m):
                if s1[i]!=s2[i]:
                    diff+=1
            if diff==2 or diff==0:
                return True
            return False
        for i in range(n):
            for j in range(i,n):
                if similar(strs[i],strs[j]):
                    adj[i].append(j)
                    adj[j].append(i)
       
        vis=[False]*n
        count=0
        def dfs(node):
            vis[node]=True
            for neb in adj[node]:
                if not vis[neb]:
                    dfs(neb)
        for i in range(n):
            if not vis[i]:
                dfs(i)
                count+=1
        return count
