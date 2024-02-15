#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, s):
        #code here
        res=[100000000]*V
        res[s]=0
        
        for i in range(V-1):
            for ed in edges:
                u=ed[0]
                v=ed[1]
                w=ed[2]
                if res[u]!=100000000:
                    if res[u]+w<res[v]:
                        res[v]=res[u]+w 
        
        for ed in edges:
            u=ed[0]
            v=ed[1]
            w=ed[2]
            if res[u]!=100000000:
                if res[u]+w<res[v]:
                    return [-1]
        return res
                        
                
