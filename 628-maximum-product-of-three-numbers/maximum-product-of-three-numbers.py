class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        no=nums.sort()

        prod1=nums[-1]*nums[-2]*nums[-3]
        prod2=nums[0]*nums[1]*nums[-1]
        return max(prod1,prod2)
