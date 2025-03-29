# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def valid_radius(radius):
            i, j = 0, 0
            while i < len(houses) and j < len(heaters):
                if abs(houses[i] - heaters[j]) <= radius:
                    i += 1
                else:
                    j += 1
            return i == len(houses)
        
        left, right = 0, max(max(houses), max(heaters))
        best = right
        while left <= right:
            mid = left + (right - left) // 2
            if valid_radius(mid):
                best = mid
                right = mid - 1
            else:
                left = mid + 1
        return best