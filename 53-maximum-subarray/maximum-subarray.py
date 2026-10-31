class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxsum=nums[0]
        currsum=0
        for i in range(len(nums)):
            currsum+=nums[i]

            maxsum=max(maxsum,currsum)

            if currsum<0:
                currsum=0
                


        return maxsum