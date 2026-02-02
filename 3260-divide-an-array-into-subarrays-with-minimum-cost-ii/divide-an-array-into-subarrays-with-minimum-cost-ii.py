from sortedcontainers import SortedList


class Solution:
  def minimumCost(self, nums: list[int], k: int, dist: int) -> int:
    
    windowSum = sum(nums[i] for i in range(1, dist + 2))
    selected = SortedList(nums[i] for i in range(1, dist + 2))
    candidates = SortedList()

    def balance() -> int:
     
      nonlocal windowSum
      while len(selected) < k - 1:
        minCandidate = candidates[0]
        windowSum += minCandidate
        selected.add(minCandidate)
        candidates.remove(minCandidate)
      while len(selected) > k - 1:
        maxSelected = selected[-1]
        windowSum -= maxSelected
        selected.remove(maxSelected)
        candidates.add(maxSelected)
      return windowSum

    windowSum = balance()
    minWindowSum = windowSum

    for i in range(dist + 2, len(nums)):
      outOfScope = nums[i - dist - 1]
      if outOfScope in selected:
        windowSum -= outOfScope
        selected.remove(outOfScope)
      else:
        candidates.remove(outOfScope)
      if nums[i] < selected[-1]: 
        windowSum += nums[i]
        selected.add(nums[i])
      else:
        candidates.add(nums[i])
      windowSum = balance()
      minWindowSum = min(minWindowSum, windowSum)

    return nums[0] + minWindowSum