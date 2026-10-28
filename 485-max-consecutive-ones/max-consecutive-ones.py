class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        onesum=0
        n=len(nums)
        maxsum=0
        j=0
        while(j<n):
            if nums[j]==1:
                onesum+=1

            else:
                maxsum=max(onesum,maxsum)
                onesum=0

            j+=1
        return max(maxsum,onesum)