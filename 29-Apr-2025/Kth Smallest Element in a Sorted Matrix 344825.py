# Problem: Kth Smallest Element in a Sorted Matrix - https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heappush(array, -matrix[i][j])
                if len(array) > k:
                    heappop(array)
        return -array[0]