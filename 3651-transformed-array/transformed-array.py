class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        
        result = []
        n = len(nums)
 
        for i, value in enumerate(nums):
            if value == 0:
              
                result.append(0)
            else:
               
                target_index = (i + value + n) % n
                result.append(nums[target_index])
              
        return result