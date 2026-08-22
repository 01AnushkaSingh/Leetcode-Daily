import math

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        
        digit_sum = sum(digits)
        
        digit_product = math.prod(digits)
        
        return n % (digit_sum + digit_product) == 0