
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.components = n

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_parent = self.find(x)
        y_parent = self.find(y)

        if x_parent == y_parent:
            return

        if self.rank[x_parent] > self.rank[y_parent]:
            self.parent[y_parent] = x_parent
        elif self.rank[x_parent] < self.rank[y_parent]:
            self.parent[x_parent] = y_parent
        else:
            self.parent[x_parent] = y_parent
            self.rank[y_parent] += 1
        self.components -= 1

    def is_single(self):
        return self.components == 1


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)

        Alice = DSU(n)
        Bob = DSU(n)
        
        added_edges = 0
        
        for edge in edges:
            edge_type, u, v = edge
            
            if edge_type == 3:
                add = False
                
                if Alice.find(u) != Alice.find(v):
                    Alice.union(u, v)
                    add = True
                    
                if Bob.find(u) != Bob.find(v):
                    Bob.union(u, v)
                    add = True
                
                if add:
                    added_edges += 1
                    
            elif edge_type == 2:
                if Bob.find(u) != Bob.find(v):
                    Bob.union(u, v)
                    added_edges += 1
            else:
                if Alice.find(u) != Alice.find(v):
                    Alice.union(u, v)
                    added_edges += 1

        if Alice.is_single() and Bob.is_single():
            return len(edges) - added_edges
        
        return -1
