# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        
        if self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        l,s = len(self.large), len(self.small)
        if l > s:
            return self.large[0]
        elif l < s :
            return -self.small[0]
        elif l > 0 and s > 0:
            return (-(self.small[0]) + self.large[0])/ 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()