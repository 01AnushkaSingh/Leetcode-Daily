
from typing import List
from math import inf

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        dp = [0] * (budget + 1)
        min_price = inf
        
        for factor, price in items:
            min_price = min(min_price, price)
            
            total_gained = sum(1 for other_factor, _ in items if other_factor % factor == 0)
            
            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + total_gained)
                
        max_items = 0
        for b in range(budget + 1):
            extra_copies = (budget - b) // min_price
            max_items = max(max_items, dp[b] + extra_copies)
            
        return max_items
