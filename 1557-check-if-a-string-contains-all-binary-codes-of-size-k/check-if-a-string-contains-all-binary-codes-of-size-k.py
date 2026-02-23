class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        needed = 1 << k
       
        got = set()
        
        
        for i in range(len(s) - k + 1):
            got.add(s[i:i+k])
           
            if len(got) == needed:
                return True
                
       
        return len(got) == needed