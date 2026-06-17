class Solution:
    def processStr(self, s: str, k: int) -> str:
      
        length = 0
        for char in s:
            if char == '*':
                length = max(0, length - 1)
            elif char == '#':
                length *= 2
            elif char != '%': 
                length += 1
           
        
       
        if k >= length:
            return '.'
        
    
        for char in reversed(s):
            if char == '*':
                length += 1
            elif char == '#':
                length //= 2
               
                if k >= length:
                    k -= length
            elif char == '%':
                
                k = length - 1 - k
            else:
                length -= 1
               
                if k == length:
                    return char