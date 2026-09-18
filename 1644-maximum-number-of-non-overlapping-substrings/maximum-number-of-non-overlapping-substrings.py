class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = [n] * 26
        right = [-1] * 26
        
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = max(right[idx], i)
            
        res = []
        last_end = -1
        
        for i in range(n):
            char_idx = ord(s[i]) - ord('a')
            if i != left[char_idx]:
                continue
                
            new_end = right[char_idx]
            j = i
            is_valid = True
            
            while j <= new_end:
                inner_idx = ord(s[j]) - ord('a')
                
                if left[inner_idx] < i:
                    is_valid = False
                    break
                new_end = max(new_end, right[inner_idx])
                j += 1
                
            if is_valid:
                if i > last_end:
                    res.append(s[i : new_end + 1])
                else:
                    res[-1] = s[i : new_end + 1]
                last_end = new_end
                
        return res
