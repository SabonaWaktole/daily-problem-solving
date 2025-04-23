# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        que = deque([])
        graph = defaultdict(list)
        degree = defaultdict(int)
        for x, y in prerequisites:
            graph[y].append(x)
            degree[x] += 1
        topsorted = []
        for i in range(numCourses):
            if not degree[i]:
                que.append(i)
        while que:
            strt = que.popleft()
            topsorted.append(strt)
            for nei in graph[strt]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    que.append(nei)
            
        return topsorted if len(topsorted) == numCourses else []
        
        
