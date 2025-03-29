# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_col(matrix, target):
            left = 0
            right = len(matrix) - 1
            
            while left <= right:
                mid = left + (right - left)//2
                if matrix[mid][0] == target:
                    return mid
                if matrix[mid][0] < target:
                    left = mid + 1
                else:
                    right = mid-1
            return right
        row = binary_col(matrix, target)
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = left + (right-left)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


