# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        for i in range(len(arr)):
            xor.append(xor[-1]^arr[i])
        xor.append(0)
        result = []
        for x,y in queries:
            result.append(xor[x]^xor[y+1])
        return result
        