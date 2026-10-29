from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        res=[]
        dequ=deque()

        for right in range(len(nums)):

            while dequ and dequ[0]<=right-k:
                dequ.popleft()

            while dequ and nums[dequ[-1]]<nums[right]:
                dequ.pop()

            dequ.append(right)

            if right>=k-1:
                res.append(nums[dequ[0]])
        return res