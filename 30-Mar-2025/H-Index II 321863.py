# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left, right = 0, n - 1
        best = 0
        
        while left <= right:
            mid = (left + right) // 2            
            if citations[mid] >= n - mid:
                best = n - mid 
                right = mid - 1
            else:
                left = mid + 1
                
        return best
