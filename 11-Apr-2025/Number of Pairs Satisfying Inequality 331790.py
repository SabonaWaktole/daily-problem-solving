# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        difference = []
        ans = 0
        for i in range(len(nums1)):
            difference.append(nums1[i] - nums2[i])
        #divide and conquer
        def merge(arr1, arr2, dif):
            nonlocal ans
            cnt = 0
            total = 0
            i, j = len(arr1) - 1, len(arr2)-1
            while i >= 0  and j >= 0:
                if arr1[i] <= arr2[j] + dif:
                    cnt += 1
                    j -= 1
                else:
                    total += (i + 1) * cnt
                    i -= 1
                    cnt = 0
            total += (i+1) * cnt
            ans += total
        def mergesort(left, right):
            if left == right:
                return [difference[left]]

            mid = left + (right-left)//2
            arr1 = mergesort(left, mid)
            arr2 = mergesort(mid+1, right)
            merge(arr1, arr2, diff)
            return sorted(arr1+arr2)
        mergesort(0, len(difference)-1)
        return ans
