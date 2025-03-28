# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def can_place(arr, dist, ball):
            cnt = 1
            init = arr[0]

            for i in range(len(arr)):
                if arr[i] - init >= dist:
                    cnt += 1
                    init = arr[i]
                if cnt >= ball:
                    return True
            if cnt >= ball:
                return True
            return False
        position.sort()
        left = 1
        right = position[-1]
        best = 1
        while left <= right:
            mid = left + (right-left) // 2
            if can_place(position, mid, m):
                left = mid+1
                best = mid
            else:
                right = mid-1
        return best
            

