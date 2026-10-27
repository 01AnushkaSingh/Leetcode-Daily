class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                temp=nums[right]
                nums[right]=nums[left]
                nums[left]= temp
                left+=1

            