class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)
        dist1=[float('inf')]*n
        dist2=[float('inf')]*n
        def bfs(dist,node,vis):
            q=deque([])
            q.append(node)
            dist[node]=0
            vis.add(node)
            while q:
                ele=q.popleft()
                if edges[ele]!=-1 and edges[ele] not in vis:
                    q.append(edges[ele])
                    dist[edges[ele]] = dist[ele] +1
                    vis.add(edges[ele])
        bfs(dist1,node1,set())
        bfs(dist2,node2,set())
        minidx=-1
        maxval=float('inf')
        for i in range(n):
            if maxval>max(dist1[i],dist2[i]):
                minidx=i
                maxval=max(dist1[i],dist2[i])
        return minidx
                
