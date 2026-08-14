from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
       
        char_count = Counter()
      
       
        max_length = 0
        left = 0
      
        
        for right, char in enumerate(s):
           
            char_count[char] += 1
          
            
            while char_count[char] > 2:
                char_count[s[left]] -= 1
                left += 1
          
           
            max_length = max(max_length, right - left + 1)
      
        return max_length
