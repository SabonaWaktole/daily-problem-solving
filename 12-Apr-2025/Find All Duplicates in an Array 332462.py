# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplic = set()
        i = 0
        while i < len(nums):
            corr = nums[i] - 1
            if i != corr:
                if nums[corr] == corr+1:
                    duplic.add(corr+1)
                    i += 1
                else:
                    nums[corr], nums[i] = nums[i], nums[corr]
            else:
                i += 1
        return list(duplic)