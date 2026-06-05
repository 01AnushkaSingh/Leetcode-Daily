from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        s2 = str(num2)
        s1 = str(num1).zfill(len(s2))
        n = len(s2)
        
        @cache
        def dfs(i: int, prev2: int, prev1: int, is_lead: bool, limit_low: bool, limit_high: bool) -> tuple[int, int]:
           
            if i == n:
              
                return 1, 0
            
           
            lo = int(s1[i]) if limit_low else 0
            hi = int(s2[i]) if limit_high else 9
            
            total_cnt = 0
            total_wave = 0
            
            for d in range(lo, hi + 1):
                next_is_lead = is_lead and (d == 0)
                
               
                wave_add = 0
                if not is_lead and prev2 != -1 and prev1 != -1:
                    if (prev2 < prev1 > d) or (prev2 > prev1 < d):
                        wave_add = 1
                
                
                next_prev2 = prev1 if not next_is_lead else -1
                next_prev1 = d if not next_is_lead else -1
                
                cnt, wave = dfs(
                    i + 1, 
                    next_prev2, 
                    next_prev1, 
                    next_is_lead, 
                    limit_low and (d == lo), 
                    limit_high and (d == hi)
                )
                
                total_cnt += cnt
               
                total_wave += wave + wave_add * cnt
                
            return total_cnt, total_wave

      
        return dfs(0, -1, -1, True, True, True)[1]