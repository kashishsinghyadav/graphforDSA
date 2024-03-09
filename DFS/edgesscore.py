class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        adj=defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i]].append(i)
        ans=0
        idx=1e5
        for key,val in adj.items():
            curr=sum(val)
            curridx=key
            
            if curr>ans:

                ans=curr
                idx=curridx
            elif curr==ans:
                idx=min(idx,curridx)
        return idx
