import math


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        odd = n * n
        even = n * (n + 1)
        return math.gcd(odd, even)