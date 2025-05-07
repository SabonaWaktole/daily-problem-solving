# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/



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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            return abs(x2 - x1) + abs(y2 - y1)
        graph = []
        dsu = DSU()
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                graph.append((distance(x1, y1, x2, y2), (x1, y1), (x2, y2)))
        graph.sort()
        weight = 0
        for w, u, v in graph:
            if not dsu.connected(u, v):
                dsu.union(u, v)
                print(u, v)
                weight += w
        return weight


