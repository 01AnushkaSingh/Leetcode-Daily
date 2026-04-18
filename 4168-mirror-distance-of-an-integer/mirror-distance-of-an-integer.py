class Solution(object):
    def mirrorDistance(self, n):
       
        def reverse(n):
            result = 0
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
            return result

        return abs(n-reverse(n))