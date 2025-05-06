# Problem: D. Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D



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



n, m, k = map(int, input().split())
dsu = DSU()
graph = set()
for _ in range(m):
    u, v = map(int, input().split())
    graph.add((u,v))
query = []
for _ in range(k):
    prompt, u, v = [x for x in input().split()]
    if prompt == 'cut':
        u, v = int(u), int(v)
        graph.discard((u,v))
        graph.discard((v, u))
    query.append([prompt, u, v])
ans = []
for x, y in graph:
    dsu.union(x, y)
# print(query)
for prompt, u, v in reversed(query):
    u, v = int(u), int(v)
    if prompt == 'cut':
        dsu.union(u, v)
        graph.add((u, v))
        
    else:
        ans.append('YES') if dsu.connected(u, v) else ans.append('NO')
    
for x in reversed(ans):
    print(x)
