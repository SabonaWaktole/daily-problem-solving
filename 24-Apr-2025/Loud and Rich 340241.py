# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1
        res = list(range(len(quiet)))
        que = deque([i for i,v in enumerate(indegree) if v == 0]) # Store vertex which has indegree 0 in que
        while que:
            vertex = que.popleft()
            for neig in graph[vertex]:
                if quiet[res[neig]] > quiet[res[vertex]]:
                    res[neig] = res[vertex]
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    que.append(neig)
            # print(res)
        return res