class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        adj=defaultdict(list)
        for i in range(len(properties)):
            for j in range(i+1,len(properties)):
                a=set(properties[i])
                b=set(properties[j])
                if len(a.intersection(b))>=k:
                    adj[i].append(j)
                    adj[j].append(i)
        # print(adj)
        def dfs(src,vis):
            vis[src]=True
            for neb in adj[src]:
                if not vis[neb]:
                    dfs(neb,vis)

        vis=[False]*len(properties)
        cnt=0
        for i in range(len(properties)):
            if not vis[i]:
                dfs(i,vis)
                cnt+=1
        return cnt

