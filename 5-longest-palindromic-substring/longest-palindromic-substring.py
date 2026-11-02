class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        T = '^#' + '#'.join(s) + '#$'
        n = len(T)
        P = [0] * n
        C = R = 0
        
        for i in range(1, n - 1):
            i_mirror = 2 * C - i 
            
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0
                
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
                
            if i + P[i] > R:
                C = i
                R = i + P[i]
                
        max_len, center_index = max((n, idx) for idx, n in enumerate(P))
        
        start = (center_index - max_len) // 2
        return s[start : start + max_len]
