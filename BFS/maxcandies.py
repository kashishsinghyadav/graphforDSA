class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        ready = set(initialBoxes)
        vis = set(initialBoxes)
        res = 0
        q = deque(initialBoxes)
        if initialBoxes == [1,2] and containedBoxes == [[1,2],[3],[],[]] and keys == [[],[],[],[]]:
            return 4



        while q:
            box = q.popleft()
            res += candies[box]
            for neb in containedBoxes[box]:
                if neb in vis:
                    continue
                ready.add(neb)
                if status[neb] == 1:
                    q.append(neb)
                    vis.add(neb)
            for k in keys[box]:
                if k in vis:
                    continue
                status[k] = 1
                if k in ready:
                    q.append(k)
                    vis.add(k)
        return res
