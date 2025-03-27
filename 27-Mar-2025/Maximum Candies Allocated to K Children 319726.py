# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        left = 1
        right = max(candies)
        
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            
            for pile in candies:
                total += pile // mid
            
            if total >= k:
                left = mid
            else:
                right = mid - 1
        
        return left