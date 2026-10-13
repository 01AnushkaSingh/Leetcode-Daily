class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(key=lambda x: x * x)
        
        n = len(nums)
        k = n // 2 
        
        s1 = sum(x * x for x in nums[:k])
        s2 = sum(x * x for x in nums[k:])
        
        return s2 - s1