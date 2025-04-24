# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for x,y in dislikes:
            graph[x-1].append(y-1)
            graph[y-1].append(x-1)
        color = [-1] * (n)
        que = deque([])
        for strt in range(n):
            if color[strt] == -1:
                color[strt] = 0
                que.append(strt)

                while que:
                    vertex = que.popleft()
                    for neig in graph[vertex]:
                        if color[neig] == -1:
                            color[neig] = 1 - color[vertex]
                            que.append(neig)
                        elif color[neig] == color[vertex]:
                            return False
        return True