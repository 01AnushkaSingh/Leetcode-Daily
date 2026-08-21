class Solution:
  def findKthSmallest(self, coins: list[int], k: int) -> int:
    sizeToLcms = self._getSizeToLcms(coins)

    def count(m: int) -> int:
      res = 0
      for sz, lcms in enumerate(sizeToLcms):
        for lcm in lcms:
          res += m // lcm * pow(-1, sz + 1)
      return res

    return bisect.bisect_left(range(k * min(coins)), k, key=count)
  def _getSizeToLcms(self, coins: list[int]) -> list[list[int]]:
    sizeToLcms = [[] for _ in range(len(coins) + 1)]
    for sz in range(1, len(coins) + 1):
      for combination in itertools.combinations(coins, sz):
        sizeToLcms[sz].append(math.lcm(*combination))
    return sizeToLcms
