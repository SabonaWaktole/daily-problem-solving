# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set()
        posDiag = set()
        res = []
        counter = 0
        def backtrack(r):
            nonlocal negDiag, posDiag, col, res, counter
            if r == n:
                counter += 1
            for c in range(n):
                if c in col or r-c in posDiag or r+c in negDiag:
                    continue
                col.add(c)
                negDiag.add(r+c)
                posDiag.add(r-c)
                

                backtrack(r+1)

                
                posDiag.remove(r-c)
                negDiag.remove(r+c)
                col.remove(c)
                
        backtrack(0)

        return counter
