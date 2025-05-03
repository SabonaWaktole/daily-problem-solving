# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = {i:i for i  in range(len(isConnected))}
        rank = {i:0 for i in range(len(isConnected))}
        def find(x):
            nonlocal parent, rank
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            nonlocal parent, rank
            r_x, r_y = find(x), find(y)
            if r_x != r_y:
                if rank[r_x] > rank[r_y]:
                    parent[r_y] = r_x
                else:
                    parent[r_x] = r_y
                    rank[r_y] = max(rank[r_y], rank[r_x]+1)
        def connected(x, y):
            nonlocal parent
            return parent[x] == parent[y]
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    union(i, j)
        comp = set()
        for i in range(len(isConnected)):
            comp.add(find(i))
        return len(comp)
        
