# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isBound(i, j):
            return i >= 0 and j >=0 and i < len(grid) and j < len(grid[0])
        direction = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        rotten = [(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2]
        time = -1
        que = deque(rotten)
        while que:
            n = len(que)
            for i in range(n):
                i,j = que.popleft()
                for up, dow in direction:
                    if isBound(up + i, dow + j) and grid[i+up][j+dow] == 1:
                        que.append((up + i, dow + j))
                        grid[i+up][j+dow] = 2
            time += 1
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    found = True
        
        return -1 if found else (time if time >= 0 else 0)