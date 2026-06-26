class Solution:
    def countMajoritySubarrays(self, nums: list[int], target: int) -> int:
   
        class BinaryIndexedTree:
            def __init__(self, size: int):
                self.tree = [0] * (size + 1)
            
            def update(self, i: int, delta: int) -> None:
                while i < len(self.tree):
                    self.tree[i] += delta
                    i += i & (-i)
            
            def query(self, i: int) -> int:
                s = 0
                while i > 0:
                    s += self.tree[i]
                    i -= i & (-i)
                return s

        n = len(nums)
       
        offset = n + 1
        bit = BinaryIndexedTree(2 * n + 1)
        
       
        bit.update(0 + offset, 1)
        
        current_sum = 0
        count = 0
        
        for num in nums:
           
            current_sum += 1 if num == target else -1
            
          
            count += bit.query(current_sum - 1 + offset)
            
            bit.update(current_sum + offset, 1)
            
        return count   