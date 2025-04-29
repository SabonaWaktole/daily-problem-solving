# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        step = 0
        heapify(nums)
        while nums[0] < k:
            min1, min2 = heappop(nums), heappop(nums)
            step += 1
            heappush(nums, min1*2 + min2)
        
        return step