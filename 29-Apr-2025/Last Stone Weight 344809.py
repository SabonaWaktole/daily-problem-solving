# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            min1, min2 = -heappop(stones), -heappop(stones)
            if min1 != min2:
                heappush(stones, min2-min1)
        return 0 if not stones else -stones[0]