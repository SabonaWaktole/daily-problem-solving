# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/


# ******* DSU Template *******
class DSU:
    def __init__(self):
        self.parent = dict()
        self.rank = defaultdict(int)

    def find(self,X):

        if X not in self.parent:
            self.parent[X] = X
            return X
        while X != self.parent[X]:
            self.parent[X] = self.parent[self.parent[X]]
            X = self.parent[X]
        return self.parent[X]
        
    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x != r_y:
            if self.rank[r_x] > self.rank[r_y]:
                self.parent[r_y] = r_x
            else:
                self.parent[r_x] = r_y
                self.rank[r_y] = max(self.rank[r_y], self.rank[r_x]+1)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    # this is to connect all nodes to their roots parent representatives
    def connect(self):
        for x in self.parent:
            self.find(x)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if len(stones) < 2:
            return 0
        
        dsu = DSU()
        x_map = defaultdict(list)
        y_map = defaultdict(list)

        for x, y in stones:
            if x_map[x]:
                dsu.union((x, y), x_map[x][0])
            if y_map[y]:
                dsu.union((x, y), y_map[y][0])

            x_map[x].append((x, y))
            y_map[y].append((x, y))
            

        
        roots = set()
        for stone in stones:
            roots.add(dsu.find(tuple(stone)))
        return len(stones) - len(roots)