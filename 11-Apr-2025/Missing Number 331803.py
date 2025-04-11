# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(((len(nums) + 1) * (len(nums)/2)) - int(sum(nums)))       
        