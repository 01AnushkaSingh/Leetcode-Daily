class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.maxSub(nums,k)-self.maxSub(nums,k-1)
    

    def maxSub(self,nums:list[int],k:int)->int:


        hashmap={}
        left=0
        count=0

        for right in range(len(nums)):
            hashmap[nums[right]]=hashmap.get(nums[right],0)+1
            while len(hashmap)>k:
                hashmap[nums[left]]-=1
                if hashmap[nums[left]]==0:
                    del hashmap[nums[left]]
                left+=1
            count+=right-left+1

        return count