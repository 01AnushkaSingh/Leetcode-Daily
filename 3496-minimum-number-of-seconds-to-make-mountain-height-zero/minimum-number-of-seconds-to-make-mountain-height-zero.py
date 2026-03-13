class Solution:
  def minNumberOfSeconds(
      self,
      mountainHeight: int,
      workerTimes: list[int]
  ) -> int:
    def getReducedHeight(m: int) -> int:
     
      return sum((-1 + math.sqrt(1 + 8 * m // workerTime)) // 2
                 for workerTime in workerTimes)

    l = 1
    r = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
    return bisect.bisect_left(range(l, r), mountainHeight,
                              key=getReducedHeight) + l