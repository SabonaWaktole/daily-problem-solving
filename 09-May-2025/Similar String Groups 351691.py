# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/



from collections import defaultdict, deque
import heapq



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
    def numSimilarGroups(self, strs: List[str]) -> int:
        def canwe(word1, word2):
            ab = []
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    ab.append(i)
            if len(ab) == 0:
                return 0 == 0

            if len(ab) != 2:
                return False
            a, b = ab
            
            if word1[a] == word2[b]:
                return True
            return False

        non_group = 0
        dsu = DSU()
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                if dsu.find(i) != dsu.find(j) and canwe(strs[i], strs[j]):
                    non_group += 1
                    dsu.union(i, j)

        return len(strs) - non_group
