class Solution:
  def stoneGameVIII(self, stones: list[int]) -> int:
    n = len(stones)
    prefix = list(itertools.accumulate(stones))
    dp = [-math.inf] * n

    dp[n - 2] = prefix[-1]

    for i in reversed(range(n - 2)):
      dp[i] = max(dp[i + 1], prefix[i + 1] - dp[i + 1])

    return dp[0]