# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        def is_rotated(arr, l, r):
            return True if arr[l] >= arr[r] else False
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if is_rotated(nums, left, right) and is_rotated(nums, mid, right):
                left = mid + 1
            elif is_rotated(nums, left, right):
                right = mid
            else:
                return nums[left]
        return nums[left]