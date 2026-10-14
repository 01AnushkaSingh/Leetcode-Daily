class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        if sum > num * 9:
            return ""
        
        n_nines = sum // 9
        remainder = sum % 9
        
       
        ans = "9" * n_nines
        if remainder > 0:
            ans += str(remainder)
        
        ans += "0" * (num - len(ans))
        
        return ans  