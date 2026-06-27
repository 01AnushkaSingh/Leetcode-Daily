class Solution:
  def maximumLength(self, nums: list[int]) -> int:
    maxNum = max(nums)
    count = collections.Counter(nums)
    ans = count[1] - (count[1] % 2 == 0) if 1 in count else 1

    for num in nums:
      if num == 1:
        continue
      length = 0
      x = num
      while x <= maxNum and x in count and count[x] >= 2:
        length += 2
        x *= x
   
      ans = max(ans, length + (1 if x in count else -1))

    return ans