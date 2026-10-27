class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        n=len(nums)
        low=0
        mid=0
        high=n-1

        while mid<=high:
            if nums[mid]==0:
                nums[mid]=nums[low]
                nums[low]=0
                mid+=1
                low+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid]=nums[high]
                nums[high]=2
                high-=1