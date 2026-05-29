class Solution:
    def minElement(self, nums: list[int]) -> int:
        min_val = float('inf')
        
        for num in nums:
            
            digit_sum = 0
            temp = num
            while temp > 0:
                digit_sum += temp % 10
                temp //= 10
            
           
            min_val = min(min_val, digit_sum)
            
        return int(min_val)