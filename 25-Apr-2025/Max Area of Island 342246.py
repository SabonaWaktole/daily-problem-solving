# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isBound(i,j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]) 
        visited = set()
        def dfs(i, j):
            nonlocal visited
            visited.add((i, j))
            area = 1
            direction = [(1,0), (0,1), (-1, 0), (0, -1)]
            for up, down in direction:
                if isBound(up+i, down+j) and (up+i, down+j) not in visited and grid[up+i][down+j]:
                    area += dfs(up+i, down+j)
            return area
        current = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not (i,j) in visited:
                    current = max(dfs(i,j), current)

        return current
