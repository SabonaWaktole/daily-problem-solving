# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        
        # Step 1: Build adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        visited = set()
        count = 0

        # Step 2: Find connected components using DFS
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)
                    stack.extend(graph[curr] - visited)
        # Step 3: Check if the component is complete
        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node, component)

                size = len(component)
                expected_edges = size * (size - 1) // 2
                actual_edges = sum(len(graph[v]) for v in component) // 2

                if expected_edges == actual_edges:
                    count += 1

        return count
