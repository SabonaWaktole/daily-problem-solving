# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        legend = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)],
        }

        def isbound(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        def canMove(from_cell, to_cell):
            
            i, j = from_cell
            a, b = to_cell
            if not isbound(a, b):
                return False
            initial = grid[i][j]
            final = grid[a][b]
            for x,y in legend[final]: 
                nx, ny = a+x, b+y
                if isbound(nx, ny) and (nx, ny) == from_cell:
                    return True
            return False



        que = deque([(0, 0)])
        visited = {(0,0)}

        while que:
            path = que.popleft()
            if path == (len(grid)-1, len(grid[0])-1):
                return True
            i, j = path
            direct = grid[i][j]

            for x, y in legend[direct]:
                to_cell = (i+x, j+y)
                if canMove(path, to_cell):
                    if to_cell not in visited:
                        que.append(to_cell)
                        visited.add(to_cell)


        return False