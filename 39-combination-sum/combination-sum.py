class Solution:

    def solve(self,index,sum,subset,nums,target,result):
        if sum==target:
            result.append(subset.copy())
            return
        elif sum>target:
            return
        if index>= len(nums):
            return

        # sum = sum+nums[index]
        subset.append(nums[index])
        self.solve(index,sum+nums[index],subset,nums,target,result)
        # sum=sum
        subset.pop()
        self.solve(index+1,sum,subset,nums,target,result)
        

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        self.solve(0,0,[],candidates,target,result)
        return result