# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(time):
            count = 0
            for r in ranks:
                count += int((time // r) ** 0.5)  # Maximum cars a mechanic can fix
                if count >= cars:
                    return True
            return False

        left, right = 1, min(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1

        return left

    
    
