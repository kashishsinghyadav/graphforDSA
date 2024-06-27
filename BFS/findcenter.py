class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        maxi=0
        idx=0
        for k,v in adj.items():
            if len(v)>maxi:
                maxi=len(v)
                idx=k
        return idx
