# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x in range(len(isConnected)):
            for y in range(len(isConnected[0])):
                if x != y:
                    graph[x].append(y)
                    graph[y].append(x)
        
        visited = set()

        def dfs(node):
            nonlocal graph, visited
            visited.add(node)
            for neig in range(len(isConnected)):
                if isConnected[node][neig] and neig not in visited:
                    dfs(neig)

        province = 0
        for vertex in range(len(isConnected)):
            if not vertex in visited:
                visited.add(vertex)
                dfs(vertex)
                province += 1
        return province



        