class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for i in nums:
            string = len(str(i))
            if (string%2 == 0):
                c= c+1
        return c