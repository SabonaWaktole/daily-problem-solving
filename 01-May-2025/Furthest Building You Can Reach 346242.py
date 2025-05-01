# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        height_difference = [heights[i+1] - heights[i] for i in range(len(heights) - 1)]
        farthest = []
        far = i = 0
        
        while far < ladders and i < len(height_difference):# The farthest building we can able to reach if we only have ladders
            if height_difference[i] > 0:
                heappush(farthest, height_difference[i])
                far += 1
            i += 1
        while i < len(height_difference):
            if height_difference[i] > 0:
                bricks -= heappushpop(farthest, height_difference[i])
            if bricks < 0:
                break
            i += 1
        
        return i
        