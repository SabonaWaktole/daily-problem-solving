# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        def dfs(i, j):
            if j < 0 or i < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return 1
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        ans = 0
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    ans += 1
                    dfs(i, j)
                    
        return ans
        