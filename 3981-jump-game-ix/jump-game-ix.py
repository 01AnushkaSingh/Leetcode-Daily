from math import inf
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        pre_max = [nums[0]] * n
        
 
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])
            
        suf_min = inf
       
        for i in range(n - 1, -1, -1):
            if i + 1 < n and pre_max[i] > suf_min:
                ans[i] = ans[i + 1]
            else:
                ans[i] = pre_max[i]
            suf_min = min(suf_min, nums[i])
            
        return ans