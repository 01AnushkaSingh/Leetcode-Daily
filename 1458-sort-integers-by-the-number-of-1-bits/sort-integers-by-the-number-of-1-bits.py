class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
       
        return sorted(arr, key=lambda num: (num.bit_count(), num))