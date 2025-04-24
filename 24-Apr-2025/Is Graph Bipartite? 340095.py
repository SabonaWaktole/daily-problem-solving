# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n
        que = deque([])
        for strt in range(n):
            if color[strt] == -1:
                que.append(strt)
                color[strt] = 0

                while que:
                    vertex = que.popleft()
                    for neig in graph[vertex]:
                        if color[neig] == -1:
                            color[neig] = 1 - color[vertex]
                            que.append(neig)
                        elif color[neig] == color[vertex]:
                            return False
        return True
