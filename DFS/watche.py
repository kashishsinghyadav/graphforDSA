class Solution:
    def watchedVideosByFriends(self, watch: List[List[str]], fnds: List[List[int]], id: int, level: int) -> List[str]:


        q=deque([])
        q.append(id)
        adj=defaultdict(list)
        n=len(watch)
        
        for i in range(n):
            for x in fnds[i]:
                adj[i].append(x)
        c=0
        vis=set()
        vis.add(id)
        while q:
            d={}
            
            l=len(q)
            for i in range(l):
                curr=q.popleft()
                for neb in adj[curr]:
                    if neb not in vis:

                        q.append(neb)
                        vis.add(neb)
                        d[neb]=watch[neb]
            c+=1
            if c==level:
                break

        ans=[]
        for i in d.values():
            for j in i:
                ans.append(j)
        
        res=Counter(ans)
        final=dict(sorted(res.items(), key=lambda item: (item[1],item[0])))
        lst=[]
        for k in final.keys():
            lst.append(k)

        return lst
            
