class Solution:
    def xorAfterQueries(self, nums: list[int], queries: list[list[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        final_mult = [1] * n
        
    
        threshold = int(n**0.5)
        
   
        small_k_queries = [ [[] for _ in range(k)] for k in range(threshold + 1)]
        
        for l, r, k, v in queries:
            if v == 1:
                continue
            if k > threshold:
               
                for i in range(l, r + 1, k):
                    final_mult[i] = (final_mult[i] * v) % MOD
            else:
               
                small_k_queries[k][l % k].append((l, r, v))
        
       
        for k in range(1, threshold + 1):
            for rem in range(k):
                if not small_k_queries[k][rem]:
                    continue
                
            
                relevant_indices = range(rem, n, k)
                idx_map = {idx: i for i, idx in enumerate(relevant_indices)}
                m = len(relevant_indices)
                
               
                diff = [1] * (m + 1)
                for l, r, v in small_k_queries[k][rem]:
                   
                    start_pos = idx_map[l]
                   
                    end_pos = (r - rem) // k
                    
                    diff[start_pos] = (diff[start_pos] * v) % MOD
                   
                    inv_v = pow(v, MOD - 2, MOD)
                    diff[end_pos + 1] = (diff[end_pos + 1] * inv_v) % MOD
                
              
                curr_v = 1
                for i in range(m):
                    curr_v = (curr_v * diff[i]) % MOD
                    actual_idx = relevant_indices[i]
                    final_mult[actual_idx] = (final_mult[actual_idx] * curr_v) % MOD
      
        ans = 0
        for i in range(n):
            ans ^= (nums[i] * final_mult[i]) % MOD
        return ans