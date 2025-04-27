# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

from collections import deque
from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def isBound(i, j):
            return 0 <= i < len(mat) and 0 <= j < len(mat[0])

        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        que = deque([(i, j) for i in range(len(mat)) for j in range(len(mat[0])) if mat[i][j] == 0])
        visited = set(que)
        length = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        level = 0
        while que:
            n = len(que)
            for _ in range(n):
                i, j = que.popleft()
                for up, dow in direction:
                    ni, nj = i + up, j + dow
                    if isBound(ni, nj) and (ni, nj) not in visited:
                        length[ni][nj] = length[i][j] + 1
                        que.append((ni, nj))
                        visited.add((ni, nj))
        return length
