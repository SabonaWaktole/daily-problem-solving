# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from bisect import bisect_right, bisect_left
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 10**9 + 7
        cnt = 0
        for i, num in enumerate(nums):
            ind = bisect_right(nums, target-num)
            cnt += (2**(ind-i-1)% MOD) if ind > i else 0
        return cnt % MOD
