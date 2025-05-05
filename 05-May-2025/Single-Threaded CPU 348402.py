# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        def print_single(times):
            for i, x in enumerate(times):
                times[i] = x + [i]
            times.sort()
            time = 0
            heap = []
            res = []
            i = 0
            while i < len(times) and times[i][0] <= time:
                heapq.heappush(heap,(times[i][1], times[i][2]))
                i += 1
            if not heap and i < len(times):
                time = times[i][0]
                heapq.heappush(heap,(times[i][1], times[i][2]))
                i += 1
            while heap:
                process, task_no = heapq.heappop(heap)
                res.append(task_no)
                time += process
                while i < len(times) and times[i][0] <= time:
                    heapq.heappush(heap,(times[i][1], times[i][2]))
                    i += 1
                if not heap and i < len(times):
                    time = times[i][0]
                    heapq.heappush(heap,(times[i][1], times[i][2]))
                    i += 1
            return res

        return print_single(tasks)