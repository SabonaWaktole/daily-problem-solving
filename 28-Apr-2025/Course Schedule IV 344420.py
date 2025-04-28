# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        prereqs = [set() for i in range(numCourses)]
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            for neig in graph[node]:
                if prereqs[node]:
                    prereqs[neig].update(prereqs[node])
                prereqs[neig].add(node)
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    queue.append(neig)
        
        ans = [x in prereqs[y] for x, y in queries]
        

        return ans
