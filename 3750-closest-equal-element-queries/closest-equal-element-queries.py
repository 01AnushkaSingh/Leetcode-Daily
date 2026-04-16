class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
       
        n = len(nums)

        doubled_length = n * 2

        
        min_distances = [doubled_length] * doubled_length

      
        last_position_left = {}
        for i in range(doubled_length):
          
            current_value = nums[i % n]

            if current_value in last_position_left:
                min_distances[i] = min(min_distances[i], i - last_position_left[current_value])

            
            last_position_left[current_value] = i

        next_position_right = {}
        for i in range(doubled_length - 1, -1, -1):
           
            current_value = nums[i % n]

        
            if current_value in next_position_right:
                min_distances[i] = min(min_distances[i], next_position_right[current_value] - i)

            
            next_position_right[current_value] = i

     
        for i in range(n):
            min_distances[i] = min(min_distances[i], min_distances[i + n])

        
        return [-1 if min_distances[query_index] >= n else min_distances[query_index]
                for query_index in queries]
