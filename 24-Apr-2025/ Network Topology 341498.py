# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict, Counter
node, edge = [int(x) for x in input().split()]
in_graph = defaultdict(int)
out_graph = defaultdict(int)

for _ in range(edge):
    a, b = [int(x) for x in input().split()]
    in_graph[a] += 1
    out_graph[b] += 1
for node in range(1, node + 1):
    in_graph[node] += out_graph[node]
arr = list(in_graph.values())

topology = Counter(arr)


if len(topology) == 2:
    if 1 in topology and topology[1] == 2 and 2 in topology:
        print("bus topology")
    elif 1 in topology and topology[1] == node - 1:
        print("star topology")
    else:
        print("unknown topology")
elif len(topology) == 1 and 2 in topology:
    print("ring topology")
else:
    print("unknown topology")

# print(topology)