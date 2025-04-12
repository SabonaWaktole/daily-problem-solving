# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isPossible(mid):
            subarrays = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > mid:
                    subarrays += 1
                    current_sum = num
                    if subarrays > k:
                        return False
            return True
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left