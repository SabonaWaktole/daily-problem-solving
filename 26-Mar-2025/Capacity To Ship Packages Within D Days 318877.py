# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def time(arr, cap):
            cur = 0
            cnt = 1 
            for x in arr:
                if cur + x > cap:
                    cnt += 1 
                    cur = x
                else:
                    cur += x
            return cnt
        
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right-left) // 2
            if time(weights, mid) <= days:
                right = mid
            else:
                left = mid + 1
        
        return left
