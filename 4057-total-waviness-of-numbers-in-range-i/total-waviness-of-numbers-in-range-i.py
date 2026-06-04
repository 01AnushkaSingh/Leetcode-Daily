class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        
        for x in range(num1, num2 + 1):
            s = str(x)
            n = len(s)
            
          
            if n < 3:
                continue
                
          
            for i in range(1, n - 1):
                if (s[i] > s[i-1] and s[i] > s[i+1]) or (s[i] < s[i-1] and s[i] < s[i+1]):
                    total_waviness += 1
                    
        return total_waviness