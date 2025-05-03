# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self,  edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1, len(edges) + 1)}
        rank = {i:0 for i in range(1, len(edges) + 1)}
        def find( x):
            nonlocal parent, rank
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
            # Write your code here
            
        def union( x, y):
            nonlocal parent, rank
            r_x = find(x)
            r_y = find(y)
            if r_x != r_y:
                if rank[r_x] > rank[r_y]:
                    parent[r_y] = r_x
                else:
                    parent[r_x] = r_y
                    rank[r_y] = max(rank[r_y], rank[r_x]+1)
                    

        def connected( x, y):
            return find(x) == find(y)
        
        for x, y in edges:
            if connected(x, y):
                return [x, y]
            union(x, y)
            
