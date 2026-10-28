class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        windowsum=0
        n=len(nums)
        maxsum=0
        count={}

        for i in range (k):
            windowsum+=nums[i]
            count[nums[i]]=count.get(nums[i],0)+1

        if len(count)==k:
            maxsum=windowsum

        for j in range(k,n):
            incoming=nums[j]
            windowsum+=incoming
            count[incoming]=count.get(incoming,0)+1

            outgoing=nums[j-k]
            windowsum-=outgoing
            count[outgoing]-=1
            if count[outgoing]==0:
                del count[outgoing]

            if len(count)==k:
                maxsum=max(maxsum,windowsum)

        return maxsum
