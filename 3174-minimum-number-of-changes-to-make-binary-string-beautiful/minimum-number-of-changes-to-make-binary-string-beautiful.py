class Solution:
    def minChanges(self, s: str) -> int:
        n = int(s, 2)

        mask = int('01' * (len(s) // 2), 2)
        
        return ((n ^ (n >> 1)) & mask).bit_count()
