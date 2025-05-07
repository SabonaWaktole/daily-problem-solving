# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E



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

n, m = map(int, input().split())
edges = []
dsu = DSU()
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
edges.sort()
weight = 0
for w, u, v in edges:
    if not dsu.connected(u, v):
        dsu.union(u, v)
        weight += w
print(weight)
