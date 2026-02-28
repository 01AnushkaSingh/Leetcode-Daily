class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        ans = 0
        for i in range(1, n + 1):
          
            bits_needed = i.bit_length()
            
            ans = (ans << bits_needed) 
            
      
            ans = (ans | i) 
            
           
            ans %= mod
            
        return ans
