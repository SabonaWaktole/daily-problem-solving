# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path):
            if len(path) == n:
                result.append("".join(path))
                return
            for ch in "abc":
                if not path or path[-1] != ch:  # Ensure no consecutive equal chars
                    backtrack(path + [ch])

        result = []
        backtrack([])
        
        return result[k - 1] if k <= len(result) else ""
