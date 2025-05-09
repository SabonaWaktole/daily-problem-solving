# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

from collections import Counter

test = int(input())
for _ in range(test):
    n, k = map(int, input().split())
    s = input()
    t = input()
    cs = Counter(s)
    ct = Counter(t)
    
    if cs != ct:
        print("NO")
        continue
    cs = {}
    ct = {}
    visited = set()

    for i in range(len(s)):
        if i + k >= len(s):
            break
        if i not in visited:
            visited.add(i)
            cs[s[i]] = cs.get(s[i], 0) + 1
        if i+k not in visited:
            visited.add(i+k)
            cs[s[i+k]] = cs.get(s[i+k], 0) + 1
        if i + k + 1 < len(s):
            if i+k+1 not in visited:
                visited.add(i+k+1)
                cs[s[i+k+1]] = cs.get(s[i+k+1], 0) + 1
    
    visited = set()
    for i in range(len(t)):
        if i + k >= len(t):
            break
        if i not in visited:
            visited.add(i)
            ct[t[i]] = ct.get(t[i], 0) + 1
        if i+k not in visited:
            visited.add(i+k)
            ct[t[i+k]] = ct.get(t[i+k], 0) + 1
        if i + k + 1 < len(t):
            if i+k+1 not in visited:
                visited.add(i+k+1)
                ct[t[i+k+1]] = ct.get(t[i+k+1], 0) + 1
    # print(cs)
    # print(ct)

    # print()
    # print()
    if cs != ct:
        print("NO")
        continue
    found = False
    for i in range(len(s)):
        if i not in visited and s[i] != t[i]:
            print('NO')
            found = True
            break
    if not found:
        print('YES')
