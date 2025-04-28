# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

from collections import defaultdict

test = int(input())
for _ in range(test):
    room = int(input())
    edge = input()
    
    one_dir = True
    for ch in edge:
        if ch == '<':
            one_dir = False
            break
    if one_dir:
        print(room)
        continue

    other_dir = True
    for ch in edge:
        if ch == '>':
            other_dir = False
            break
    if other_dir:
        print(room)
        continue

    ans = 0
    for i in range(room):
        if edge[i] == '-' or edge[(i - 1) % room] == '-':
            ans += 1
    print(ans)
