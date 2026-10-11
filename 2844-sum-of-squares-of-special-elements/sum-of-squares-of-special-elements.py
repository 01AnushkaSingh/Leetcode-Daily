class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(num**2 for i, num in enumerate(nums)
               if len(nums) % (i + 1) == 0)