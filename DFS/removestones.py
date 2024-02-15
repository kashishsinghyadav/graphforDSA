class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        vis=set()
        count=0
        def dfs(src):
            vis.add(src)

            for v in stones:
                val=tuple(v)
                if val not in vis:
                    nr=v[0]
                    nc=v[1]
                    if src[0]==nr or src[1]==v[1]:
                        
                        dfs(val)
                        vis.add(val)




        for i in stones:
            val=tuple(i)
            if val not in vis:
                dfs(val)
                count+=1
        return len(stones)-count
        
