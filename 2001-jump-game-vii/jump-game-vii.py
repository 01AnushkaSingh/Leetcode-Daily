class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
      
       
        prefix_sum = [0] * (n + 1)
        prefix_sum[1] = 1 
      
     
        reachable = [True] + [False] * (n - 1)  
      
       
        for i in range(1, n):
          
            if s[i] == "0":
               
                left_bound = max(0, i - maxJump)
                right_bound = i - minJump
              
              
                if left_bound <= right_bound:
                    count_reachable = prefix_sum[right_bound + 1] - prefix_sum[left_bound]
                    reachable[i] = count_reachable > 0
          
           
            prefix_sum[i + 1] = prefix_sum[i] + (1 if reachable[i] else 0)
      
      
        return reachable[-1]