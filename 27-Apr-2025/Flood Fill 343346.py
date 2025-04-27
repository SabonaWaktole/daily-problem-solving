# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def isBound(i, j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])

        direction = [(0,1), (0,-1), (1,0), (-1,0)]
        key = image[sr][sc]
        que = deque([(sr, sc)])
        image[sr][sc] = color
        visited = set()
        while que:
            i, j = que.popleft()
            for up, dow in direction:
                if isBound(i+up, j+dow) and (i+up, j+dow) not in visited and image[i+up][j+dow] == key:
                    image[i+up][j+dow] = color
                    que.append((i+up, j+dow))
                    visited.add((i+up, j+dow))
        return image
