class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countzero=0
        countone=0
        counttwo=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                countzero+=1
            elif nums[i]==1:
                countone+=1
            else:
                counttwo+=1

        i=0
        while (countzero>0):
            nums[i]=0
            i+=1
            countzero-=1
        while (countone>0):
            nums[i]=1
            i+=1
            countone-=1
        while (counttwo>0):
            nums[i]=2
            i+=1
            counttwo-=1