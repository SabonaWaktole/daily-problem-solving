# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def isBound(i,j):
            return 0 <= i and 0 <= j and i < len(isWater) and j < len(isWater[0])
        directions = [(0,1), (0, -1), (-1,0), (1,0)]
        que = deque([(i,j) for i in range(len(isWater)) for j in range(len(isWater[0])) if isWater[i][j]])
        height = [[0 for i in range(len(isWater[0]))] for j in range(len(isWater))]
        level = 0
        visited = set()
        while que:
            n = len(que)
            for cell in range(n):
                i, j = que.popleft()
                visited.add((i,j))
                height[i][j] = level
                for up, dow in directions:
                    if isBound(i+up, j+dow) and (i+up, j+dow) not in visited and isWater[i+up][dow+j] == 0:
                        que.append((i+up, j+dow))
                        visited.add((i+up, j+dow))
            level += 1
        return height