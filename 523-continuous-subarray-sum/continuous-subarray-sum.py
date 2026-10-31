class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        mapp={0:-1}
        summ=0
        for i in range(len(nums)):
            summ+=nums[i]
            rem=summ%k
            if rem in mapp:
                if i - mapp[rem]>=2:
                    return True
            else:
                mapp[rem]=i
        return False
