# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = set()
        lit = [0,0]
        mic = set(nums)

        for i in range(len(nums)):
            if nums[i] not in dic:
                dic.add(nums[i])
            else:
                lit[0] = nums[i]
            if i not in mic:
                lit[1] = i
        if lit[1] == 0:
            lit[1] = len(nums) 
        return lit