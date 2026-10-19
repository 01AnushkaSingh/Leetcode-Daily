class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = nums.count(target)
        lessThan = sum(num < target for num in nums)
        return [i for i in range(lessThan, lessThan + count)]
        