# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        ans = [set() for i in range(n)]
        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            node = queue.popleft()
            for neig in graph[node]:
                if ans[node]:
                    ans[neig].update(ans[node])
                ans[neig].add(node)
                indegree[neig] -= 1
                if indegree[neig] == 0:
                    queue.append(neig)

        ans = [sorted(ans[i]) for i in range(n)]
        return ans