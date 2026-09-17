class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        
        ans = float('inf')
        window_sum = 0
        left = 0
        
        for right in range(n):
            window_sum += arr[right]
            
            while window_sum > target:
                window_sum -= arr[left]
                left += 1
                
            if window_sum == target:
                current_len = right - left + 1
                
                if left > 0 and best[left - 1] != float('inf'):
                    ans = min(ans, best[left - 1] + current_len)
                
                best[right] = min(best[right], current_len)
            
            if right > 0:
                best[right] = min(best[right], best[right - 1])
                
        return ans if ans != float('inf') else -1
