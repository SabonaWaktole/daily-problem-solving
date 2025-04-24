# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i, x in enumerate(manager):
            if x != -1:
                graph[x].append(i)
        def dfs(emp):
            if not graph[emp]:
                return 0
            return informTime[emp] + max(dfs(sub) for sub in graph[emp])

        return dfs(headID)