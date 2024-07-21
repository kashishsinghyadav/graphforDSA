class Solution:
    def buildMatrix(self, k: int, row: List[List[int]], col: List[List[int]]) -> List[List[int]]:
        adjrow=defaultdict(list)
        indeg1=[0]*(k+1)
        for u,v in row:
            adjrow[u].append(v)
            indeg1[v]+=1
        adjcol=defaultdict(list)
        indeg2=[0]*(k+1)
        for u,v in col:
            adjcol[u].append(v)
            indeg2[v]+=1
        q1=deque([])
        q2=deque([])
        for i in range(1,len(indeg1)):
            if indeg1[i]==0:
                q1.append(i)
        for i in range(1,len(indeg2)):
            if indeg2[i]==0:
                q2.append(i)
        ans1=[]
        ans2=[]
        while q1:
            curr=q1.popleft()
            ans1.append(curr)
            for neb in adjrow[curr]:
                indeg1[neb]-=1
                if indeg1[neb]==0:
                    q1.append(neb)
        while q2:
            curr=q2.popleft()
            ans2.append(curr)
            for neb in adjcol[curr]:
                indeg2[neb]-=1
                if indeg2[neb]==0:
                    q2.append(neb)
        # print(ans1)
        # print(ans2)
        if len(ans1)!=k or len(ans2)!=k:
            return []
        ans = [[0] * k for _ in range(k)]

        for row, val in enumerate(ans1):
            col = ans2.index(val)
            ans[row][col] = val
            
        return ans
