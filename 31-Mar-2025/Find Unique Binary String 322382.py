# Problem: Find Unique Binary String - https://leetcode.com/problems/find-unique-binary-string/description/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numbers = set(nums)
        number = ''
        def backtrack(num, n):
            nonlocal numbers, number
            intnum = "".join(num)
            if len(num) == n and not  intnum in numbers:
                number = intnum
                return
            elif len(num) == n:
                return 
            num.append("0")
            backtrack(num, n)
            num.pop()

            num.append("1")
            backtrack(num, n)
            num.pop()

        backtrack([], len(nums[0]))
        return number

        