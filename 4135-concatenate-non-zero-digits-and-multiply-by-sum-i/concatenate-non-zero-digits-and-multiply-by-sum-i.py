class Solution:
    def sumAndMultiply(self, n: int) -> int:
       
        s = str(n)
        
       
        x_str = "".join(digit for digit in s if digit != '0')
        
        
        if not x_str:
            return 0
            
        x = int(x_str)
        
        
        digit_sum = sum(int(digit) for digit in x_str)
        
       
        return x * digit_sum