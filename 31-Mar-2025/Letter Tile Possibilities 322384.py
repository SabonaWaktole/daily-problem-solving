# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Python code
        def num_tile_possibilities(tiles):
            def backtrack(path, counter):
                if path:
                    sequences.add(path)
                for char in counter:
                    if counter[char] > 0:
                        counter[char] -= 1
                        backtrack(path + char, counter)
                        counter[char] += 1

            sequences = set()
            counter = Counter(tiles)
            backtrack("", counter)
            return len(sequences)
        return num_tile_possibilities(tiles)