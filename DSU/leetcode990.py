class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        rank = [0 for i in range(26)]

        def find(val, parent):
            if parent[val] == val:
                return val
            else:
                parent[val] = find(parent[val], parent)
                return parent[val]

        def union(x, y):
            px = find(x, parent)
            py = find(y, parent)
            if px == py:
                return
            if rank[px] > rank[py]:
                parent[py] = parent[px]
            elif rank[px] < rank[py]:
                parent[px] = parent[py]
            else:
                parent[px] = parent[py]
                rank[py] += 1

        for s in equations:
            if s[1] == '=':
                union(ord(s[0]) - ord('a'), ord(s[3]) - ord('a'))

        for s in equations:
            if s[1] == '!':
                if find(ord(s[0]) - ord('a'), parent) == find(ord(s[3]) - ord('a'), parent):
                    return False

        return True
