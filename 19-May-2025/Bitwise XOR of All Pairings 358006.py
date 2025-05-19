# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

# from functools import reduce

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        if n % 2 and m % 2:
            nums1 += nums2
            return reduce(xor, (nums1))
        elif n % 2:
            return reduce(xor, nums2)
        elif m % 2:
            return reduce(xor, nums1)
        else:
            return 0
