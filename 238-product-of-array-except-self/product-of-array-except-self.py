class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans=[0]*n
        ans[0]=1

        for i in range(1,n):
            ans[i]=nums[i-1]*ans[i-1]

        rightpro=1
        for i in range(n-1,-1,-1):
            ans[i]*=rightpro
            rightpro*=nums[i]
            
        return ans
