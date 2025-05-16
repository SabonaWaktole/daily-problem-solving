# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
    
        left = 0
        max_len = 0
        cur = 0
        for right in range(len(nums)):
            while cur & nums[right]:
                cur = cur ^ nums[left]
                left += 1

            max_len = max(max_len, right - left + 1)
            cur = cur | nums[right]
            

        return max_len