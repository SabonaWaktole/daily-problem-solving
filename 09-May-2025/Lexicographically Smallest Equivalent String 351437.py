# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

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


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        represent = defaultdict(str)
        dsu = DSU()
        for i in range(len(s1)):
            dsu.union(s1[i], s2[i])
            rep1 = represent[s1[i]] if represent[s1[i]] else 'z'
            rep2 = represent[s2[i]] if represent[s2[i]] else 'z'
            min_ = min([s1[i], s2[i], rep1, rep2])
            root = dsu.find(s1[i])
            if root in represent and represent[root]:
                min_ = min(represent[root], min_)
            represent[dsu.find(s1[i])] = min_
            
        last = []
        for i, x in enumerate(baseStr):
            if represent[dsu.find(x)]:
                last.append(represent[dsu.find(x)]) 
            else:
                last.append(x)
        return "".join(last)