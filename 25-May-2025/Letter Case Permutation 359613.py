# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        result = set()

        for i in range(2 ** n):
            bits = f"{i:0{n}b}" 
            chars = list(s)

            for j in range(n):
                if bits[j] == '1' and chars[j].isalpha():
                    chars[j] = chars[j].swapcase()

            result.add((''.join(chars)))

        return list(result)