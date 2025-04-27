# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        que = deque([0])
        while que:
            room = que.popleft()
            visited.add(room)
            for neig in rooms[room]:
                if neig not in visited:
                    que.append(neig)
        return len(visited) == len(rooms)