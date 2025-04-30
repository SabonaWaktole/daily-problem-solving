# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

from collections import defaultdict, deque

def find_alphabet_order(names):
    graph = defaultdict(set)
    indegree = {chr(c): 0 for c in range(ord('a'), ord('z')+1)}

    n = len(names)
    for i in range(n - 1):
        name1, name2 = names[i], names[i+1]
        min_len = min(len(name1), len(name2))
        found = False

        for j in range(min_len):
            c1, c2 = name1[j], name2[j]
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].add(c2)
                    indegree[c2] += 1
                found = True
                break
        if not found and len(name1) > len(name2):
            return "Impossible"

    # Topological sort
    q = deque([c for c in indegree if indegree[c] == 0])
    result = []

    while q:
        c = q.popleft()
        result.append(c)
        for nei in graph[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    if len(result) != 26:
        return "Impossible"
    return ''.join(result)


n = int(input())
names = [input() for _ in range(n)]
print(find_alphabet_order(names))
