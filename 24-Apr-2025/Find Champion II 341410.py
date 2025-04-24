# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        winner = set(range(n))
        for x, y in edges:
            if y in winner:
                winner.remove(y)
        if len(winner) > 1:
            return -1
        winner = list(winner)
        return winner[0]
