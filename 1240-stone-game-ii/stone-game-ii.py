from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
      
        suffix_sums = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sums[i] = suffix_sums[i + 1] + piles[i]
            
        @lru_cache(None)
        def dfs(i, M):
    
            if i + 2 * M >= n:
                return suffix_sums[i]

            min_opponent_score = float('inf')
            for X in range(1, 2 * M + 1):
                min_opponent_score = min(min_opponent_score, dfs(i + X, max(M, X)))
                
            return suffix_sums[i] - min_opponent_score
            
        return dfs(0, 1)      