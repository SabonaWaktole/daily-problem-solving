# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mismatch = set()
        i = 0
        while i < len(nums):
            corr = nums[i]-1
            if i != corr:
                if nums[corr] == corr+1:
                    mismatch.add(corr+1)
                    i += 1
                else:
                    nums[corr], nums[i] = nums[i], nums[corr]
            else:
                i += 1
        mismatch = list(mismatch)
        tot = sum(nums) - (mismatch[0])
        mismatch.append((int((len(nums)+1) * len(nums)))//2 - tot)
        print(mismatch)
        return mismatch

