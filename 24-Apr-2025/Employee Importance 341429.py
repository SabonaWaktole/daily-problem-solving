# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        for person in employees:
            graph[person.id] = [person.importance, person.subordinates]
        que = deque([id])
        importance = 0
        while que:
            vertex = que.popleft()
            importance += graph[vertex][0]
            for neig in graph[vertex][1]:
                que.append(neig)
        return importance