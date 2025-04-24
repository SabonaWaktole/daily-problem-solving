# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    from collections import deque
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        que = deque([])
        back_graph = defaultdict(list)
        outgoing = defaultdict(int)
        for i, vertex in enumerate(graph):
            outgoing[i] += len(vertex)
            for edge in vertex:
                back_graph[edge].append(i)
        
        for i in range(len(graph)):
            if not graph[i]:
                que.append(i)
        order = []
        print(back_graph)
        print(que)
        while que:
            strt = que.popleft()
            order.append(strt)
            for x in back_graph[strt]:
                outgoing[x] -= 1
                if outgoing[x] == 0:
                    que.append(x)
        return sorted(order)