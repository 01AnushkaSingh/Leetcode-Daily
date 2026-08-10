class Solution:
    def winnerSquareGame(self, n: int) -> bool:
       
        from functools import cache
      
        @cache
        def can_win(remaining_stones: int) -> bool:
           
            
            if remaining_stones == 0:
                return False
          
   
            square_root = 1
            while square_root * square_root <= remaining_stones:
                stones_to_remove = square_root * square_root
              
                
                if not can_win(remaining_stones - stones_to_remove):
                    return True
                  
                square_root += 1
          
           
            return False
      
      
        return can_win(n)
