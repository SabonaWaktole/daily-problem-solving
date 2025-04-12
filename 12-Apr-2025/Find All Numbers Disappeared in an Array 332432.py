# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        kn = len(nums)
        ret = []
        nums = set(nums)
        for x in range(1,kn + 1):
            if x not in nums:
                ret.append(x)
        return ret 
    