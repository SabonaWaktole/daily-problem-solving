# Problem: The Number of the Smallest Unoccupied Chair - https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        for i, time in enumerate(times):
            time.append(i)
            times[i] = time
        times.sort()
        unoccopied = list(range(len(times)))
        occopied = []
        for friend in times:
            while occopied and occopied[0][0] <= friend[0]:
               heappush(unoccopied, heappop(occopied)[1])
            if friend[2] == targetFriend:
                return heappop(unoccopied)
            heappush(occopied, (friend[1], heappop(unoccopied)))
        return targetFriend