# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
            indegree[x] += 1
            indegree[y] += 1
        que = deque([x for x in range(n) if indegree[x] == 1])
        visited = set()
        ans = []
        while que:
            size = len(que)
            ans = []
            for i in range(size):
                node = que.popleft()
                ans.append(node)
                for neig in graph[node]:
                    indegree[neig] -= 1
                    if indegree[neig] == 1:
                        que.append(neig)
        return ans
