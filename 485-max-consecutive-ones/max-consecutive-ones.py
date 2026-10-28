class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        onesum=0
        n=len(nums)
        maxsum=0
        j=0
        for num in nums:
            if nums[j]==1:
                onesum+=1
                maxsum=max(onesum,maxsum)

            else:
                
                onesum=0

            j+=1
        return maxsum