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



# class Solution:
#     def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        
#         def topological_sort(graph):
#             indegree = defaultdict(int)
            
            
#             for node in graph:
#                 for neighbor in graph[node]:
#                     indegree[neighbor] += 1
            
            
#             queue = deque([node for node in graph if indegree[node] == 0])
            
#             sorted_order = []
            
            
#             while queue:
#                 node = queue.popleft()
#                 sorted_order.append(node)
                
#                 for neighbor in graph[node]:
#                     indegree[neighbor] -= 1
#                     if indegree[neighbor] == 0:
#                         queue.append(neighbor)
            
            
#             if len(sorted_order) != len(graph):
#                 return []  
            
#             return sorted_order
#         new_group = m
#         for i in range(n):
#             if group[i] == -1:
#                 new_group += 1
#                 group[i] = new_group
        
#         def build_sub_graph(grp):
#             graph = defaultdict(list)
#             for i, neig in enumerate(beforeItems):
#                 for node in neig:
#                     if group[node] == group[i] and group[i] == grp:
#                         graph[node].append(i)
#             return graph
        

#         def goup_to_graph_mapper():
#             grouping = defaultdict(list)
#             for i, x in enumerate(group):
#                 grouping[x].append(i)
#             return grouping
        
        
#         def grouping_graph():
#             group_graph = defaultdict(set)
#             for i, neig in enumerate(beforeItems):
#                 for node in neig:
#                     if group[node] != group[i]:
#                         group_graph[group[node]].add(group[i])
#             return group_graph
        
        
#         sorted_group = topological_sort(grouping_graph())
#         # print(sorted_group, "is dependent group")
#         # print(topological_sort(build_sub_graph(2)))

#         grouped_graph = goup_to_graph_mapper()
        

#         ans = []
#         visited = set()
#         for grp in sorted_group:
#             if len(grouped_graph[grp]) > 1:
#                     ans.extend(topological_sort(build_sub_graph(grp)))
#             else:
#                 ans.extend(grouped_graph[grp])
#             visited.add(grp)

#         for grp in range(new_group+1):
#             if not grp in visited:
#                 if len(grouped_graph[grp]) > 1:
#                     ans.extend(topological_sort(build_sub_graph(grp)))
#                 else:
#                     ans.extend(grouped_graph[grp])
#         return ans 
        



            
                


        
        
#         # graph = defaultdict(set)
#         # new_group = m
#         # for i in range(n):
#         #     if group[i] == -1:
#         #         new_group += 1
#         #         group[i] = new_group
        
#         # for i, before in enumerate(beforeItems):
#         #     for j in before:
#         #         if group[i] != group[j]:
#         #             graph[group[j]].add(group[i])
        
#         # group_sorted = topological_sort(graph)
#         # if not group_sorted:
#         #     return []  

#         # item_graph = defaultdict(set)
#         # item_indegree = {i: 0 for i in range(n)}
        
#         # for i, before in enumerate(beforeItems):
#         #     for j in before:
#         #         if group[i] == group[j]:
#         #             item_graph[j].add(i)
#         #             item_indegree[i] += 1
        
#         # item_sorted = defaultdict(list)
#         # for grp in set(group):
#         #     group_items = [i for i in range(n) if group[i] == grp]
#         #     item_subgraph = {i: item_graph[i] for i in group_items}
#         #     item_sorted_grp = topological_sort(item_subgraph)
#         #     if not item_sorted_grp:
#         #         return []  
#         #     item_sorted[grp] = item_sorted_grp
        
#         # result = []
#         # for grp in group_sorted:
#         #     result.extend(item_sorted[grp])
        
#         # return result
