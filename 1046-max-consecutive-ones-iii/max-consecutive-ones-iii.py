class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        maxlen=0
        czero=0
        left=0
        for right in range(len(nums)):
            
           
             
                if nums[right]==0:
                    czero+=1
                while czero>k:
                    
                    if nums[left]==0:
                        czero-=1
                    left+=1
                maxlen=max(maxlen,right-left+1)
        return maxlen