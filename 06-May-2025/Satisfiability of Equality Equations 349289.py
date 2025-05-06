# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

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
    def equationsPossible(self, equations: List[str]) -> bool:
        dsu = DSU()
        for string in equations:
            if string[1:3] == "==":
                fir, sec = string[0], string[3]
                dsu.union(fir, sec)
        for string in equations:
            fir, sec = string[0], string[3]
            if string[1:3] == '!=' and dsu.connected(fir, sec):
                return False
            elif string[1:3] == '==' and not dsu.connected(fir, sec):
                return False
        return True
                  