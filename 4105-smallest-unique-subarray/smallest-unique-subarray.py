from collections import Counter
from typing import List


class Solution:

  def smallestUniqueSubarray(self, nums: List[int]) -> int:
    n = len(nums)

    BASE1, MOD1 = 100003, 1_000_000_007
    BASE2, MOD2 = 100019, 1_000_000_009

    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    for i in range(1, n + 1):
      pow1[i] = (pow1[i - 1] * BASE1) % MOD1
      pow2[i] = (pow2[i - 1] * BASE2) % MOD2

    def has_unique_subarray(length: int) -> bool:
        counts = Counter()
        h1 = 0
        h2 = 0

        for i in range(length):
            h1 = (h1 * BASE1 + nums[i]) % MOD1
            h2 = (h2 * BASE2 + nums[i]) % MOD2

        counts[(h1, h2)] += 1

        high_pow1 = pow1[length - 1]
        high_pow2 = pow2[length - 1]

        for i in range(length, n):
            h1 = ((h1 - nums[i - length] * high_pow1) * BASE1 + nums[i]) % MOD1
            h2 = ((h2 - nums[i - length] * high_pow2) * BASE2 + nums[i]) % MOD2
            counts[(h1, h2)] += 1

        return any(freq == 1 for freq in counts.values())

    left, right = 1, n
    ans = n

    while left <= right:
      mid = (left + right) // 2
      if has_unique_subarray(mid):
        ans = mid
        right = mid - 1  
      else:
        left = mid + 1  

    return ans
