class Solution:
    def minOperations(self, s: str) -> int:
        
        operations_start_with_zero = 0
      
        for index, char in enumerate(s):
           
            expected_char = '01'[index & 1]  
          
           
            if char != expected_char:
                operations_start_with_zero += 1
      
       
        operations_start_with_one = len(s) - operations_start_with_zero
      
        
        return min(operations_start_with_zero, operations_start_with_one)