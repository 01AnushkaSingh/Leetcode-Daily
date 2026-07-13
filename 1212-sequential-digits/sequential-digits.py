class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        sample = "123456789"
        nums = []
        
        
        low_len = len(str(low))
        high_len = len(str(high))
        
       
        for length in range(low_len, high_len + 1):
            
            for i in range(9 - length + 1):
                num = int(sample[i : i + length])
                
               
                if low <= num <= high:
                    nums.append(num)
                    
        return nums
   