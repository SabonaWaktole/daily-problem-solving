# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        graph = defaultdict(int)
        back_graph = defaultdict(int)
        cands = []
        for x, y in trust:
            graph[y] += 1
            back_graph[x] += 1
        for y in graph:
            if graph[y] == n-1 and back_graph[y] == 0:
                return y
        return -1