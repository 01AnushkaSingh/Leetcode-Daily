class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minNum = min(nums)
        maxNum = max(nums)
        numSet = set(nums)
        result = []
        for num in range(minNum, maxNum + 1):
            if num not in numSet:
                result.append(num)
        return result