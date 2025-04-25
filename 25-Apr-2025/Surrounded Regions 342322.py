# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isBound(i, j):
            return i >= 0 and j >= 0 and i < len(board) and j < len(board[0])
        
        visited = set()
        def dfs(i, j):
            direction = [(1,0), (0, 1), (-1,0), (0, -1)]
            visited.add((i, j))
            for up, dow in direction:
                ni, nj = i + up, j + dow
                if isBound(ni, nj) and (ni, nj) not in visited and board[ni][nj] == 'O':
                    dfs(i+up, j+dow)
        # Left edge
        for i in range(len(board)):
            if board[i][0] == 'O':
                dfs(i, 0)

        # Top edge
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                dfs(0, j)

        # Right edge
        for i in range(len(board)):
            if board[i][len(board[0])-1] == 'O':
                dfs(i, len(board[0])-1)

        # Bottom edge
        for j in range(len(board[0])):
            if board[len(board)-1][j] == 'O':
                dfs(len(board)-1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'