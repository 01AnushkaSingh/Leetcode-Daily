from collections import defaultdict
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = min(cost for _, cost in items)
        max_factor = max(factor for factor, _ in items)
        
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1
            
        for i in range(1, max_factor + 1):
            if freq[i] > 0:
                for multiple in range(2 * i, max_factor + 1, i):
                    freq[i] += freq[multiple]
                    
        cost_count = defaultdict(int)
        for factor, cost in items:
            available_pairs = freq[factor] - 1
            if available_pairs > 0 and cost <= 2 * cheapest:
                cost_count[cost] += available_pairs
                
        total_items = 0
        for cost in sorted(cost_count):
            count = cost_count[cost]
            buy = min(count, budget // cost)
            total_items += 2 * buy
            budget -= buy * cost
            
        total_items += budget // cheapest
        
        return total_items
