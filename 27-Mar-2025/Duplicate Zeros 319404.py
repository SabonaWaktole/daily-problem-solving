# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        cnt = 0
        left = len(arr)-1
        
        cnt = arr.count(0)
        arr.extend([0]*cnt)
        right = len(arr)-1
        while left >= 0:
            if arr[left] == 0:
                right -= 2
                left -= 1
            else:
                arr[left], arr[right] = arr[right], arr[left]
                left -= 1
                right -= 1
        arr[:] = arr[:-cnt] if cnt else arr
        
