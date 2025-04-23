# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = {source}
        def dfs(i):
            if i == destination:
                return True
            for neighbour in graph[i]:
                if not neighbour in visited:
                    visited.add(neighbour)
                    if dfs(neighbour):
                        return True
            return False
        return dfs(source)