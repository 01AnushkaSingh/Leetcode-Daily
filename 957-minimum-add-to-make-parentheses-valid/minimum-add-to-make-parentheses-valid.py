class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        unmatched_close = 0
        
        for char in s:
            if char == '(':
                open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    unmatched_close += 1
                    
        return open_brackets + unmatched_close
