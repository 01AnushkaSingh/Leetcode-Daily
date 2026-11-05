class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2.sort()  
        count = 0
        
        for x in arr1:
            target_low = x - d
            target_high = x + d
            
            left, right = 0, len(arr2) - 1
            found_invalid_neighbor = False
            
            while left <= right:
                mid = (left + right) // 2
                
                if target_low <= arr2[mid] <= target_high:
                    found_invalid_neighbor = True
                    break
                elif arr2[mid] < target_low:
                    left = mid + 1
                else:
                    right = mid - 1
            
            if not found_invalid_neighbor:
                count += 1
                
        return count
