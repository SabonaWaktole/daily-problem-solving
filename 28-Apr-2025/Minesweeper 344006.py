# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        direction = [(1,0), (1,1), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        def isBound(i, j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        def isValid(i, j):
            nonlocal direction
            mine = 0
            for x,y in direction:
                ni, nj = i+x, j+y
                if isBound(ni, nj) and  board[ni][nj] == 'M':
                    mine += 1
            return [not(bool(mine)), mine]
        que = deque([])
        visited = set()
        que.append((click[0], click[1]))
        while que:
            i, j = que.popleft()
            visited.add((i, j))
            valid, mine = isValid(i, j)
            if valid:
                board[i][j] = 'B'
                for x, y in direction:
                    ni, nj = i+x, j+y
                    if isBound(ni, nj) and ((ni, nj)) not in visited:
                        que.append((ni, nj))
                        visited.add((ni, nj))
            else:
                board[i][j] = str(mine)

            

        return board