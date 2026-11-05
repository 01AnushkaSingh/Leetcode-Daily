class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for i in range(len(arr1)):
            is_valid = True  
            for j in range(len(arr2)):
                diff = abs(arr1[i] - arr2[j])
                if diff <= d:
                    is_valid = False  
                    break 
            
            if is_valid:
                count += 1  

        return count
