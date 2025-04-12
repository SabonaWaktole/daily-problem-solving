# Problem: Find the Duplicate Number - https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            corr = nums[i]-1
            if i != corr:
                if nums[corr] == corr+1:
                    return corr + 1
                else:
                    nums[corr], nums[i] = nums[i], nums[corr]
            else:
                i += 1