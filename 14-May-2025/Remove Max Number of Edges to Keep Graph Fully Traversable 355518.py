# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/



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
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = DSU()
        bob = DSU()
        a_type = None
        b_type = None
        edge_to_remove = 0
        for t, u, v in edges:
            if t == 3:
                a_type = b_type = u
                if alice.connected(u, v):
                    edge_to_remove += 1
                else:
                    alice.union(u, v)
                    bob.union(u, v)
        for t, u, v in edges:
            if t == 2:
                if bob.connected(u, v):
                    edge_to_remove += 1
                
                bob.union(u, v)
                b_type = u
            elif t == 1:
                a_type = u

                if alice.connected(u, v):
                    edge_to_remove += 1
                alice.union(u, v)
        for i in range(1, n+1):
            if not alice.connected(a_type, i) or not bob.connected(b_type, i):
                return -1
        return edge_to_remove 