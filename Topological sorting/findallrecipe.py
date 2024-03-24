class Solution:
    def findAllRecipes(self, recipes: List[str], ingre: List[List[str]], supplies: List[str]) -> List[str]:
        graph=defaultdict(list)
        indeg=defaultdict(int)
        for rec,indg in zip(recipes,ingre):
            indeg[rec]=len(indg)
            for ind in indg:
                graph[ind].append(rec)
        # print(graph)
        # print(indeg)
        ans=[]
        q=deque(supplies)
        
        recipe=set(recipes)
        while q:
            supply=q.popleft()
            if supply in recipe:
                ans.append(supply)
            for rec in graph[supply]:
                indeg[rec] -= 1
                if indeg[rec]==0:
                    q.append(rec)
        return ans

        # adj=dict()
        # supply=set(supplies)
        # for i in range(len(recipes)):
        #     adj[recipes[i]]=ingre[i]
        # # print(adj)
        # def bfs(src):
        #     q=deque([])
        #     q.append(src)
            
        #     while q:
        #         ele=q.popleft()
        #         for neb in adj[ele]:
        #             if neb not in supply:
        #                 return False 
                    
        #     supply.add(src)
        #     return True


        
        # ans=[]
        # for rec in recipes:
        #     if bfs(rec):
        #         ans.append(rec)
        # return ans
        
        
