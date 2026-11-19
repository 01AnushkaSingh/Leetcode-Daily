class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        min1 = min2 = min3 = float('inf')
        max1 = max2 = max3 = float('-inf')
        
        for x in nums:
            if x < min1:
                min3, min2, min1 = min2, min1, x
            elif x < min2:
                min3, min2 = min2, x
            elif x < min3:
                min3 = x
                
            if x > max1:
                max3, max2, max1 = max2, max1, x
            elif x > max2:
                max3, max2 = max2, x
            elif x > max3:
                max3 = x
                
        return min(
            max1 - min3,  
            max3 - min1, 
            max2 - min2   
        )
