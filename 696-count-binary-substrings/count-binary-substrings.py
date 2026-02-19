class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        ans = 0
        prevCount = 0
        currentCount = 1

        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                currentCount += 1
            else:
                
                ans += min(prevCount, currentCount)
                prevCount = currentCount
                currentCount = 1
        
      
        ans += min(prevCount, currentCount)
        return ans
