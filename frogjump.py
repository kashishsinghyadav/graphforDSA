class Solution:
    def canCross(self, stones) -> bool:
        hashmap={}
        for st in stones:
           hashmap[st]=set()
        hashmap[stones[0]].add(1)

        for i in range(len(stones)):
            curr=stones[i]
            for h in hashmap[curr]:
                nxt=curr+h
                if nxt == stones[-1]:return True
                if nxt in stones:

                    if h-1>0:
                        hashmap[nxt].add(h-1)
                    hashmap[nxt].add(h)
                    hashmap[nxt].add(h+1)


        return False
    
stones = [0,1,3,5,6,8,12,17]
A =Solution()
print(A.canCross(stones))