class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
       
        
        previous_bit = -1
      
       
        while n > 0:
            
            current_bit = n & 1
        
            if previous_bit == current_bit:
                return False
          
           
            previous_bit = current_bit
          
            
            n >>= 1
      
       
        return True