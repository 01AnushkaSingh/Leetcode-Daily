

class Solution:
    def minOperations(self, s):
        if all(s[i] <= s[i+1] for i in range(len(s) - 1)):
                return 0
        if len(s) == 2:
            return -1
        mn, mx = min(s), max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        if any(c in [mn, mx] for c in s[1:-1]):
            return 2
        return 3