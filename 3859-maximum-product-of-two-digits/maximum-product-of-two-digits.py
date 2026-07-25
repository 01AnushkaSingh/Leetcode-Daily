class Solution:
    def maxProduct(self, n: int) -> int:
        no=sorted(str(n))
    
        

        return int(no[-1])*int(no[-2])