class Solution(object):
    def zigZagArrays(self, n, l, r):
      
        MOD = 10**9+7
        r -= l
        dp = [1]*(r+1)
        for _ in range(n-1):
            prefix = 0
            for i in range(len(dp)):
                dp[i], prefix = prefix, (prefix+dp[i])%MOD
            dp.reverse()
        return (reduce(lambda accu, x: (accu+x)%MOD, dp, 0)*2)%MOD
