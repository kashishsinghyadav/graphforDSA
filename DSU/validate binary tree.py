class Solution:
    def validateBinaryTreeNodes(self, n: int, left: List[int], right: List[int]) -> bool:
        adj=defaultdict(list)
        parent=[ i for i in range(n)]
        c=n
        def find(x):
            if parent[x]==x:
                return x
            parent[x]=find(parent[x])
            return parent[x]
        def union(p,child):
            nonlocal c
            if find(child)!=child:
                return False
            if find(p)==child:
                return False
            parent[child]=p
            c-=1
            return True

        
        for i in range(n):
            if left[i]!=-1 and union(i,left[i])==False:
                return False
            if right[i]!=-1 and union(i,right[i])==False:
                return False
        return c==1

              
