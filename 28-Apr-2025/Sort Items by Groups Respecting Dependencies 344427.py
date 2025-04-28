# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque

        def topological_sort(nodes, graph):
            indegree = {node: 0 for node in nodes}
            for u in graph:
                for v in graph[u]:
                    indegree[v] += 1

            queue = deque([node for node in nodes if indegree[node] == 0])
            sorted_order = []

            while queue:
                u = queue.popleft()
                sorted_order.append(u)

                for v in graph[u]:
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        queue.append(v)

            return sorted_order if len(sorted_order) == len(nodes) else []

        new_group = m
        for i in range(n):
            if group[i] == -1:
                group[i] = new_group
                new_group += 1

        def build_sub_graph(grp, grouped_graph):
            graph = defaultdict(list)
            nodes = grouped_graph[grp]
            for i in nodes:
                for node in beforeItems[i]:
                    if group[node] == group[i]:
                        graph[node].append(i)
            return nodes, graph

        def goup_to_graph_mapper():
            grouping = defaultdict(list)
            for i, x in enumerate(group):
                grouping[x].append(i)
            return grouping

        def grouping_graph():
            group_graph = defaultdict(set)
            for i, neig in enumerate(beforeItems):
                for node in neig:
                    if group[node] != group[i]:
                        group_graph[group[node]].add(group[i])
            return group_graph

        grouped_graph = goup_to_graph_mapper()
        group_graph = grouping_graph()

        groups = list(grouped_graph.keys())
        sorted_group = topological_sort(groups, group_graph)
        if not sorted_group:
            return []

        ans = []

        for grp in sorted_group:
            if not grouped_graph[grp]:
                continue
            nodes, sub_graph = build_sub_graph(grp, grouped_graph)
            sorted_nodes = topological_sort(nodes, sub_graph)
            if not sorted_nodes:
                return []
            ans.extend(sorted_nodes)

        return ans


