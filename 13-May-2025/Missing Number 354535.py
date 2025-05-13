# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0
        for i, x in enumerate(nums):
            result ^= i+1
            result ^= x
        return result