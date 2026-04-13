import math

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        min_dist = math.inf
        
        for i, num in enumerate(nums):
            if num == target:
                
                current_dist = abs(i - start)
                if current_dist < min_dist:
                    min_dist = current_dist
                    
        return min_dist
