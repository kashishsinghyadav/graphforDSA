class Solution:
    def findCircleNum(self, con: List[List[int]]) -> int:
        n=len(con)

        vis=set()
        count=0


        def dfs(src):
            vis.add(src)

            for nbr in range(n):
                if con[src][nbr]==1 and nbr not in vis:
                    dfs(nbr)



        for i in range(n):
            if i not in vis:
                dfs(i)
                count+=1
        return count
