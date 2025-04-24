# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #White -> 0, Gray -> 1, Black -> 2
        graph = defaultdict(list)
        for x, y in prerequisites:
            graph[y].append(x)
        print(graph)
        color = [0] * numCourses
        valid = True
        visited = set()
        def dfs(vertex):
            nonlocal valid, visited
            visited.add(vertex)
            # exit condition 
            if not valid:
                return False
            color[vertex] = 1
            for neig in graph[vertex]:
                if color[neig] == 0:
                    color[neig] = 1
                    dfs(neig)
                elif color[neig] == 1:
                    valid = False
            color[vertex] = 2
        for vertex in range(numCourses):
            if vertex not in visited:
                dfs(vertex)
        return valid
        
            