# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        sum_array = []
        for i, row in enumerate(grid):
            row = [-x for x in row]
            heapify(row)
            for j in range(limits[i]):
                heappush(sum_array, -heappop(row))
                if len(sum_array) > k:
                    heappop(sum_array)
        return sum(sum_array)