class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        mx = max(nums)
        total_sum = sum(nums)
        
        return mx * n - total_sum
