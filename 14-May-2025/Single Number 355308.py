# Problem: Single Number - https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for x in nums:
            res ^= x
        return res